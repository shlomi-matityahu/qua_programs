# %%
import os
from pathlib import Path
import numpy as np
from qualang_tools.config.waveform_tools import drag_gaussian_pulse_waveforms
from qualang_tools.units import unit
import copy

#######################
# AUXILIARY FUNCTIONS #
#######################
u = unit(coerce_to_integer=True)

######################
# Network parameters #
######################
qop_ip = "10.1.1.11"  # Write the QM router IP address
cluster_name = 'carmel_gilboa'  # Write your cluster_name if version >= QOP220

#####################
# OPX configuration #
#####################
# CW pulse parameter
const_len = 16
const_amp = 300 * u.mV

#############################################
#                  Qubits                   #
#############################################
qubit_rotation_keys = ["x180", "x180_flux_spec", "x90", "minus_x90", "y180", "y90", "minus_y90"]

# Constants for Pi Pulse
PI_LENGTH = 40
PI_SIGMA = PI_LENGTH / 5
PI_LENGTH_FLUX_SPEC = 100
PI_SIGMA_FLUX_SPEC = PI_LENGTH_FLUX_SPEC / 5

# Constants for each qubit (replace example values with actual values)
qubit1_IF=0.0
QUBIT_CONSTANTS = {
    "q1_xy": {
        "amplitude": 0.125, 
        "pi_len": PI_LENGTH,
        "pi_sigma": PI_SIGMA,
        "pi_len_flux_spec": PI_LENGTH_FLUX_SPEC,
        "pi_sigma_flux_spec": PI_SIGMA_FLUX_SPEC,
        "anharmonicity": -200 * u.MHz,
        "drag_coefficient": 0.5,
        "ac_stark_shift": 0.0 * u.MHz,
        "LO": 6.05 * u.GHz,  # Example LO frequency
        "IF": 50 * u.MHz,    # Example IF frequency
        "con": "con1",
        "fem": 1,
        "ao": 2
    },
    "q2_xy": {
        "amplitude": 0.5,
        "pi_len": PI_LENGTH,
        "pi_sigma": PI_SIGMA, 
        "pi_len_flux_spec": PI_LENGTH_FLUX_SPEC,
        "pi_sigma_flux_spec": PI_SIGMA_FLUX_SPEC,
        "anharmonicity": -180 * u.MHz,
        "drag_coefficient": 0.5,
        "ac_stark_shift": 0.0 * u.MHz,
        "LO": 6.0 * u.GHz,  
        "IF": 50 * u.MHz,
        "con": "con1",
        "fem": 1,
        "ao": 3   
    },
    "q3_xy": {
        "amplitude": 0.130,
        "pi_len": PI_LENGTH,
        "pi_sigma": PI_SIGMA, 
        "pi_len_flux_spec": PI_LENGTH_FLUX_SPEC,
        "pi_sigma_flux_spec": PI_SIGMA_FLUX_SPEC,
        "anharmonicity": -190 * u.MHz,
        "drag_coefficient": 0.5,
        "ac_stark_shift": 0.0 * u.MHz,
        "LO": 6.05 * u.GHz,  
        "IF": 50 * u.MHz,
        "con": "con1",
        "fem": 1,
        "ao": 4    
    },
    "q4_xy": {
        "amplitude": 0.120,
        "pi_len": PI_LENGTH,
        "pi_sigma": PI_SIGMA, 
        "pi_len_flux_spec": PI_LENGTH_FLUX_SPEC,
        "pi_sigma_flux_spec": PI_SIGMA_FLUX_SPEC,
        "anharmonicity": -185 * u.MHz,
        "drag_coefficient": 0.5,
        "ac_stark_shift": 0.0 * u.MHz,
        "LO": 5.95 * u.GHz,  
        "IF": 50 * u.MHz,
        "con": "con1",
        "fem": 1,
        "ao": 5    
    },
   
}

# Relaxation time
qb_reset_time = 50_000

# Saturation_pulse
saturation_len = 20 * u.us
saturation_amp = 0.45

def generate_waveforms(rotation_keys):
    """ Generate all necessary waveforms for a set of rotation types across all qubits. """
    
    if not isinstance(rotation_keys, list):
        raise ValueError("rotation_keys must be a list")

    waveforms = {}

    for qubit_key, constants in QUBIT_CONSTANTS.items():
        amp = constants["amplitude"]
        pi_len = constants["pi_len"]
        pi_sigma = constants["pi_sigma"]
        pi_len_flux_spec = constants["pi_len_flux_spec"]
        pi_sigma_flux_spec = constants["pi_sigma_flux_spec"]
        drag_coef = constants["drag_coefficient"]
        ac_stark_shift = constants["ac_stark_shift"]
        anharmonicity = constants["anharmonicity"]

        for rotation_key in rotation_keys:
            if rotation_key in ["x180", "x180_flux_spec", "y180"]:
                wf_amp = amp
            elif rotation_key in ["x90", "y90"]:
                wf_amp = amp / 2
            elif rotation_key in ["minus_x90", "minus_y90"]:
                wf_amp = -amp / 2
            else:
                continue

            wf, der_wf = np.array(drag_gaussian_pulse_waveforms(wf_amp, pi_len, pi_sigma, drag_coef, anharmonicity, ac_stark_shift))

            if rotation_key == "x180_flux_spec":
                wf, der_wf = np.array(drag_gaussian_pulse_waveforms(wf_amp, pi_len_flux_spec, pi_sigma_flux_spec, drag_coef, anharmonicity, ac_stark_shift))
                I_wf = wf
                Q_wf = der_wf
            elif rotation_key.startswith("x") or rotation_key == "minus_x90":
                I_wf = wf
                Q_wf = der_wf
            else:  # y rotations
                I_wf = (-1) * der_wf
                Q_wf = wf

            waveforms[f"{qubit_key}_{rotation_key}_I"] = I_wf
            waveforms[f"{qubit_key}_{rotation_key}_Q"] = Q_wf

    return waveforms

# Generate waveforms for all qubits
waveforms = generate_waveforms(qubit_rotation_keys)

##########################################
#               Flux line                #
##########################################
FLUX_CONSTANTS = {
    "q1_z": {
        "idle_point": 0.01,
        "con": "con1",
        "fem": 4,
        "ao": 1,
        "iir": [],
        "fir": [],
        "delay": 0,
        "unipolar_flux_len": 200,
        "unipolar_flux_amp": 0.11
    },
    

}

flux_settle_time = 200
feedforward_taps=[1.0,0.0]
feedback_tap=[0.0]
#feedforward_taps=[1.2290982325589284*0.99, -0.89035179401475628*0.98]
#feedback_tap=[0.665*0.99]
#############################################
#                Resonators                 #
#############################################
readout_len = 100
rr_reset_time = 2_000
pump_len = 200
pump_amp = {
    "TWPA1": 0.45,
    "TWPA2": 0.35
}

RL_CONSTANTS = {
    "rl1": {
        "LO": 6.45 * u.GHz,  # Example LO frequency
        "RESONATORS": ["q1_rr"],
        "TWPA": "TWPA1",
        "TWPA_LO": 8 * u.GHz,
        "TWPA_IF": 40e6,
        "TOF": 296,
        "rl_con": "con1",
        "rl_fem": 1,
        "rl_ao": 2,
        "rl_ai": 1,
        "twpa_con": "con1",
        "twpa_fem": 2,
        "twpa_ao": 2,
    } 
   
}

# add r1_twin

RR_CONSTANTS = {
    "q1_rr": {
        "amplitude": 0.01, 
        "midcircuit_amplitude": 0.01, 
        "IF": 50 * u.MHz,    # Example IF frequency
        "rotation_angle": (0.0 / 180) * np.pi,
        "ge_threshold": 0.0,
        "midcircuit_rotation_angle": (0.0 / 180) * np.pi,
        "midcircuit_ge_threshold": 0.0
    },
    "q2_rr": {
        "amplitude": 0.04, 
        "midcircuit_amplitude": 0.04, 
        "IF": 50 * u.MHz,    # Example IF frequency
        "rotation_angle": (0.0 / 180) * np.pi,
        "ge_threshold": 0.0,
        "midcircuit_rotation_angle": (0.0 / 180) * np.pi,
        "midcircuit_ge_threshold": 0.0,
    },
    
}

RR_CONSTANTS["q1_rr_twin"] = copy.deepcopy(RR_CONSTANTS["q1_rr"])
RR_CONSTANTS["q1_rr_twin"]["amplitude"] = 0.0
RR_CONSTANTS["q1_rr_twin"]["midcircuit_rotation_angle"] = ( 0.0 / 180 ) * np.pi
RR_CONSTANTS["q1_rr_twin"]["midcircuit_ge_threshold"] = 0.0

opt_weights = False
opt_weights_plot = False
if opt_weights:
    from qualang_tools.config.integration_weights_tools import convert_integration_weights
    current_file_path = os.path.dirname(os.path.abspath(__file__))
    # weights_q1_rr = np.load(os.path.join(current_file_path, "optimal_weights_q1_rr.npz"))
    # weights_q2_rr = np.load(os.path.join(current_file_path, "optimal_weights_q2_rr.npz"))
    # weights_q3_rr = np.load(os.path.join(current_file_path, "optimal_weights_q3_rr.npz"))
    # weights_q4_rr = np.load(os.path.join(current_file_path, "optimal_weights_q4_rr.npz"))
    # weights_q5_rr = np.load(os.path.join(current_file_path, "optimal_weights_q5_rr.npz"))
    # weights_q6_rr = np.load(os.path.join(current_file_path, "optimal_weights_q6_rr.npz"))
    # weights_q7_rr = np.load(os.path.join(current_file_path, "optimal_weights_q7_rr.npz"))

    # OPT_WEIGHTS = {
    #     "q1_rr": {
    #         "real": convert_integration_weights(weights_q1_rr["weights_real"], plot=opt_weights_plot),
    #         "minus_imag": convert_integration_weights(weights_q1_rr["weights_minus_imag"], plot=opt_weights_plot),
    #         "imag": convert_integration_weights(weights_q1_rr["weights_imag"], plot=opt_weights_plot),
    #         "minus_real": convert_integration_weights(weights_q1_rr["weights_minus_real"], plot=opt_weights_plot)
    #     },
    #     "q2_rr": {
    #         "real": convert_integration_weights(weights_q2_rr["weights_real"], plot=opt_weights_plot),
    #         "minus_imag": convert_integration_weights(weights_q2_rr["weights_minus_imag"], plot=opt_weights_plot),
    #         "imag": convert_integration_weights(weights_q2_rr["weights_imag"], plot=opt_weights_plot),
    #         "minus_real": convert_integration_weights(weights_q2_rr["weights_minus_real"], plot=opt_weights_plot)
    #     },
    #     "q3_rr": {
    #         "real": convert_integration_weights(weights_q3_rr["weights_real"], plot=opt_weights_plot),
    #         "minus_imag": convert_integration_weights(weights_q3_rr["weights_minus_imag"], plot=opt_weights_plot),
    #         "imag": convert_integration_weights(weights_q3_rr["weights_imag"], plot=opt_weights_plot),
    #         "minus_real": convert_integration_weights(weights_q3_rr["weights_minus_real"], plot=opt_weights_plot)
    #     },
    #     "q4_rr": {
    #         "real": convert_integration_weights(weights_q4_rr["weights_real"], plot=opt_weights_plot),
    #         "minus_imag": convert_integration_weights(weights_q4_rr["weights_minus_imag"], plot=opt_weights_plot),
    #         "imag": convert_integration_weights(weights_q4_rr["weights_imag"], plot=opt_weights_plot),
    #         "minus_real": convert_integration_weights(weights_q4_rr["weights_minus_real"], plot=opt_weights_plot)
    #     },
    #     "q5_rr": {
    #         "real": convert_integration_weights(weights_q5_rr["weights_real"], plot=opt_weights_plot),
    #         "minus_imag": convert_integration_weights(weights_q5_rr["weights_minus_imag"], plot=opt_weights_plot),
    #         "imag": convert_integration_weights(weights_q5_rr["weights_imag"], plot=opt_weights_plot),
    #         "minus_real": convert_integration_weights(weights_q5_rr["weights_minus_real"], plot=opt_weights_plot)
    #     },
    #     "q6_rr": {
    #         "real": convert_integration_weights(weights_q6_rr["weights_real"], plot=opt_weights_plot),
    #         "minus_imag": convert_integration_weights(weights_q6_rr["weights_minus_imag"], plot=opt_weights_plot),
    #         "imag": convert_integration_weights(weights_q6_rr["weights_imag"], plot=opt_weights_plot),
    #         "minus_real": convert_integration_weights(weights_q6_rr["weights_minus_real"], plot=opt_weights_plot)
    #     },
    #     "q7_rr": {
    #         "real": convert_integration_weights(weights_q7_rr["weights_real"], plot=opt_weights_plot),
    #         "minus_imag": convert_integration_weights(weights_q7_rr["weights_minus_imag"], plot=opt_weights_plot),
    #         "imag": convert_integration_weights(weights_q7_rr["weights_imag"], plot=opt_weights_plot),
    #         "minus_real": convert_integration_weights(weights_q7_rr["weights_minus_real"], plot=opt_weights_plot)
    #     },
    # }

    # OPT_WEIGHTS["q1_rr_twin"] = copy.deepcopy(OPT_WEIGHTS["q1_rr"])
else:
    OPT_WEIGHTS = {
        "q1_rr": {
            "real": [(1.0, readout_len)],
            "minus_imag": [(1.0, readout_len)],
            "imag": [(1.0, readout_len)],
            "minus_real": [(1.0, readout_len)]
        },
        "q2_rr": {
            "real": [(1.0, readout_len)],
            "minus_imag": [(1.0, readout_len)],
            "imag": [(1.0, readout_len)],
            "minus_real": [(1.0, readout_len)]
        },
        
    }
    OPT_WEIGHTS["q1_rr_twin"] = copy.deepcopy(OPT_WEIGHTS["q1_rr"])

#######################
# Terminal Flux Pulse #
#######################

terminal_flux_len = 500
terminal_flux_amp = 0.125

# %%
        
#############################################
#                  Config                   #
#############################################
config = {
    "version": 1,
    "controllers": {
        "con1": {
            "type": "opx1000",
            "fems": {
                # NOTE: BANDS ARE GOING TO CHANGE ONCE WE GET THE FREQUENCIES FROM AWS !!!
                1: {
                    "type": "MW",
                    "analog_outputs": {
                        1: {"sampling_rate": 1e9, "full_scale_power_dbm": 6, "band": 2}, # q0
                        2: {"sampling_rate": 1e9, "full_scale_power_dbm": 6, "band": 2}, # q1 XY
                        3: {"sampling_rate": 1e9, "full_scale_power_dbm": 6, "band": 2}, # q2 XY
                        4: {"sampling_rate": 1e9, "full_scale_power_dbm": 10, "band": 2}, # q3 XY
                        5: {"sampling_rate": 1e9, "full_scale_power_dbm": 6, "band": 2}, # q4 XY
                        6: {"sampling_rate": 1e9, "full_scale_power_dbm": 6, "band": 2}, # q5
                        7: {"sampling_rate": 1e9, "full_scale_power_dbm": 6, "band": 2}, # q6 
                        8: {"sampling_rate": 1e9, "full_scale_power_dbm": 6, "band": 2}, # q7



                    },
                    "analog_inputs": {
                        1: {"sampling_rate": 1e9, "band": 2, "gain_db": 0},  # RL1
                    },
                },
                5: {
                    "type": "LF",
                    "analog_outputs": {
                        1: {"sampling_rate": 2e9,"offset": 0.0, "output_mode":"amplified"},
                        3: {"sampling_rate": 1e9,"offset": 0.0, "output_mode":"direct"},
                        2: {"sampling_rate": 1e9,"offset": 0.00, "upsampling_mode":"pulse","output_mode":"amplified","filter":{"feedforward": [],"feedback":[]}},
                        4: {"sampling_rate": 1e9,"offset": 0.0, "upsampling_mode":"mw", "output_mode":"direct"},
                        8: {"offset": -0.1,"upsampling_mode":"mw","output_mode":"direct"},
                    },
                },
            },
        },
    },
    "elements": {
        

        # readout line 1
        **{rr: {
            "MWInput": {
                "port": (RL_CONSTANTS["rl1"]["rl_con"], RL_CONSTANTS["rl1"]["rl_fem"], RL_CONSTANTS["rl1"]["rl_ao"]),
                "oscillator_frequency": RL_CONSTANTS["rl1"]["LO"],  # in Hz [6-8e9]
            },
            "intermediate_frequency": RR_CONSTANTS[rr]["IF"],  # in Hz [-350e6, +350e6]
            "MWOutput": {
                "port": (RL_CONSTANTS["rl1"]["rl_con"], RL_CONSTANTS["rl1"]["rl_fem"], RL_CONSTANTS["rl1"]["rl_ai"]),
            },
			'time_of_flight': RL_CONSTANTS["rl1"]["TOF"],
            'smearing': 0,
            "operations": {
                "cw": "const_pulse",
                "readout": "readout_pulse_"+rr,
                "midcircuit_readout": "midcircuit_readout_pulse_"+rr,
            },
        } for rr in RL_CONSTANTS["rl1"]["RESONATORS"]},

      
        # xy drives
        **{qubit_key: {
            "MWInput": {
                "port": (QUBIT_CONSTANTS[qubit_key]["con"], QUBIT_CONSTANTS[qubit_key]["fem"], QUBIT_CONSTANTS[qubit_key]["ao"]),
                "oscillator_frequency": QUBIT_CONSTANTS[qubit_key]["LO"],  # in Hz
            },
            "intermediate_frequency": QUBIT_CONSTANTS[qubit_key]["IF"],  # in Hz
            "operations": {
                "zero": "zero_pulse",
                "cw": "const_pulse",
                "saturation": "saturation_pulse",
                "x180": f"x180_pulse_{qubit_key}",
                "x180_flux_spec": f"x180_flux_spec_pulse_{qubit_key}",
                "x90": f"x90_pulse_{qubit_key}",
                "-x90": f"-x90_pulse_{qubit_key}",
                "y90": f"y90_pulse_{qubit_key}",
                "y180": f"y180_pulse_{qubit_key}",
                "-y90": f"-y90_pulse_{qubit_key}",
            },
        } for qubit_key in QUBIT_CONSTANTS.keys()},

        # flux lines
    
     
    }, 
    "pulses": {
         "const_pulse_single": {
            "operation": "control",
            "length": const_len,
            "waveforms": {
                "single": "const_wf",
            }
         },
            "4ns_pulse_single": {
            "operation": "control",
            "length": const_len,
            "waveforms": {
                "single": "4ns_wf",
            },
         },
          "1ns_pulse_single": {
            "operation": "control",
            "length": const_len,
            "waveforms": {
                "single": "1ns_wf",
            },
         },
        "flux_pulse": {
            "operation": "control",
            "length": terminal_flux_len,
            "waveforms": {
                "single": "terminal_flux_wf",
            },
        },
        **{f"unipolar_flux_pulse_{key}":
            {
                "operation": "control",
                "length": FLUX_CONSTANTS[key]["unipolar_flux_len"],
                "waveforms": {
                    "single": f"unipolar_flux_wf_{key}",
                }
            }
            for key in FLUX_CONSTANTS.keys()
        },
        **{f"netzero_flux_pulse_{key}":
            {
                "operation": "control",
                "length": FLUX_CONSTANTS[key]["unipolar_flux_len"],
                "waveforms": {
                    "single": f"netzero_flux_wf_{key}",
                }
            }
            for key in FLUX_CONSTANTS.keys()
        },
        "const_pulse": {
            "operation": "control",
            "length": const_len,
            "waveforms": {
                "I": "const_wf",
                "Q": "zero_wf",
            }
        },
        "4ns_pulse": {
            "operation": "control",
            "length": const_len,
            "waveforms": {
                "I": "4ns_wf",
                "Q": "zero_wf",
            },
        },
        "1ns_pulse": {
            "operation": "control",
            "length": const_len,
            "waveforms": {
                "I": "1ns_wf",
                "Q": "zero_wf",
            },
        },
        "zero_pulse": {
            "operation": "control",
            "length": 16,
            "waveforms": {
                "I": "zero_wf",
                "Q": "zero_wf",
            },
        },
        "saturation_pulse": {
            "operation": "control",
            "length": saturation_len,
            "waveforms": {
                "I": "saturation_wf",
                "Q": "zero_wf",
            },
        },
        **{f"x90_pulse_{key}":
            {
                "operation": "control",
                "length": PI_LENGTH,
                "waveforms": {
                    "I": f"x90_I_wf_{key}",
                    "Q": f"x90_Q_wf_{key}"
                }
            }
            for key in QUBIT_CONSTANTS.keys()
        },
        **{f"x180_pulse_{key}":
            {
                "operation": "control",
                "length": PI_LENGTH,
                "waveforms": {
                    "I": f"x180_I_wf_{key}",
                    "Q": f"x180_Q_wf_{key}"
                }
            }
            for key in QUBIT_CONSTANTS.keys()
        },
        **{f"x180_flux_spec_pulse_{key}":
            {
                "operation": "control",
                "length": PI_LENGTH_FLUX_SPEC,
                "waveforms": {
                    "I": f"x180_flux_spec_I_wf_{key}",
                    "Q": f"x180_flux_spec_Q_wf_{key}"
                }
            }
            for key in QUBIT_CONSTANTS.keys()
        },
        **{f"-x90_pulse_{key}":
            {
                "operation": "control",
                "length": PI_LENGTH,
                "waveforms": {
                    "I": f"minus_x90_I_wf_{key}",
                    "Q": f"minus_x90_Q_wf_{key}"
                }
            }
            for key in QUBIT_CONSTANTS.keys()
        },
        **{f"y90_pulse_{key}":
            {
                "operation": "control",
                "length": PI_LENGTH,
                "waveforms": {
                    "I": f"y90_I_wf_{key}",
                    "Q": f"y90_Q_wf_{key}"
                }
            }
            for key in QUBIT_CONSTANTS.keys()
        },
        **{f"y180_pulse_{key}":
            {
                "operation": "control",
                "length": PI_LENGTH,
                "waveforms": {
                    "I": f"y180_I_wf_{key}",
                    "Q": f"y180_Q_wf_{key}"
                }
            }
            for key in QUBIT_CONSTANTS.keys()
        },
        **{f"-y90_pulse_{key}":
            {
                "operation": "control",
                "length": PI_LENGTH,
                "waveforms": {
                    "I": f"minus_y90_I_wf_{key}",
                    "Q": f"minus_y90_Q_wf_{key}"
                }
            }
            for key in QUBIT_CONSTANTS.keys()
        },

        **{
            f"readout_pulse_{key}": {
                "operation": "measurement",
                "length": readout_len,
                "waveforms": {
                    "I": f"readout_wf_{key}",
                    "Q": "zero_wf"
                },
                "integration_weights": {
                    "cos": "cosine_weights",
                    "sin": "sine_weights",
                    "minus_sin": "minus_sine_weights",
                    "rotated_cos": f"rotated_cosine_weights_{key}",
                    "rotated_sin": f"rotated_sine_weights_{key}",
                    "rotated_minus_sin": f"rotated_minus_sine_weights_{key}",
                    "opt_cos": f"opt_cosine_weights_{key}",
                    "opt_sin": f"opt_sine_weights_{key}",
                    "opt_minus_sin": f"opt_minus_sine_weights_{key}",
                },
                "digital_marker": "ON",
            } for key in RR_CONSTANTS.keys()
        },
        **{
            f"midcircuit_readout_pulse_{key}": {
                "operation": "measurement",
                "length": readout_len,
                "waveforms": {
                    "I": f"midcircuit_readout_wf_{key}",
                    "Q": "zero_wf"
                },
                "integration_weights": {
                    "cos": "cosine_weights",
                    "sin": "sine_weights",
                    "minus_sin": "minus_sine_weights",
                    "rotated_cos": f"midcircuit_rotated_cosine_weights_{key}",
                    "rotated_sin": f"midcircuit_rotated_sine_weights_{key}",
                    "rotated_minus_sin": f"midcircuit_rotated_minus_sine_weights_{key}",
                    "opt_cos": f"midcircuit_opt_cosine_weights_{key}",
                    "opt_sin": f"midcircuit_opt_sine_weights_{key}",
                    "opt_minus_sin": f"midcircuit_opt_minus_sine_weights_{key}",
                },
                "digital_marker": "ON",
            } for key in RR_CONSTANTS.keys()
        },
    },
    "waveforms": {
        "const_wf": {"type": "constant", "sample": const_amp},
        "4ns_wf":{"type": "arbitrary", "samples": [const_amp]*4+[0]*(const_len-4)},
        "1ns_wf":{"type": "arbitrary", "samples": [const_amp]*1+[0]*(const_len-1)},
        "saturation_wf": {"type": "constant", "sample": saturation_amp},
        "terminal_flux_wf": {"type": "constant", "sample": terminal_flux_amp},
        **{f"unipolar_flux_wf_{key}": {"type": "constant", "sample": FLUX_CONSTANTS[key]["unipolar_flux_amp"]} for key in FLUX_CONSTANTS.keys()},
        **{f"netzero_flux_wf_{key}": {"type": "arbitrary", "samples": [FLUX_CONSTANTS[key]["unipolar_flux_amp"]] * int(FLUX_CONSTANTS[key]["unipolar_flux_len"] / 2) + [-FLUX_CONSTANTS[key]["unipolar_flux_amp"]] * int(FLUX_CONSTANTS[key]["unipolar_flux_len"] / 2)} for key in FLUX_CONSTANTS.keys()},
        "zero_wf": {"type": "constant", "sample": 0.0},
        **{f"x90_I_wf_{key}": {"type": "arbitrary", "samples": waveforms[key+"_x90_I"].tolist()} for key in QUBIT_CONSTANTS.keys()},
        **{f"x90_Q_wf_{key}": {"type": "arbitrary", "samples": waveforms[key+"_x90_Q"].tolist()} for key in QUBIT_CONSTANTS.keys()},
        **{f"x180_I_wf_{key}": {"type": "arbitrary", "samples": waveforms[key+"_x180_I"].tolist()} for key in QUBIT_CONSTANTS.keys()},
        **{f"x180_Q_wf_{key}": {"type": "arbitrary", "samples": waveforms[key+"_x180_Q"].tolist()} for key in QUBIT_CONSTANTS.keys()},
        **{f"x180_flux_spec_I_wf_{key}": {"type": "arbitrary", "samples": waveforms[key+"_x180_flux_spec_I"].tolist()} for key in QUBIT_CONSTANTS.keys()},
        **{f"x180_flux_spec_Q_wf_{key}": {"type": "arbitrary", "samples": waveforms[key+"_x180_flux_spec_Q"].tolist()} for key in QUBIT_CONSTANTS.keys()},
        **{f"minus_x90_I_wf_{key}": {"type": "arbitrary", "samples": waveforms[key+"_minus_x90_I"].tolist()} for key in QUBIT_CONSTANTS.keys()},
        **{f"minus_x90_Q_wf_{key}": {"type": "arbitrary", "samples": waveforms[key+"_minus_x90_Q"].tolist()} for key in QUBIT_CONSTANTS.keys()},
        **{f"y90_I_wf_{key}": {"type": "arbitrary", "samples": waveforms[key+"_y90_I"].tolist()} for key in QUBIT_CONSTANTS.keys()},
        **{f"y90_Q_wf_{key}": {"type": "arbitrary", "samples": waveforms[key+"_y90_Q"].tolist()} for key in QUBIT_CONSTANTS.keys()},
        **{f"y180_I_wf_{key}": {"type": "arbitrary", "samples": waveforms[key+"_y180_I"].tolist()} for key in QUBIT_CONSTANTS.keys()},
        **{f"y180_Q_wf_{key}": {"type": "arbitrary", "samples": waveforms[key+"_y180_Q"].tolist()} for key in QUBIT_CONSTANTS.keys()},
        **{f"minus_y90_I_wf_{key}": {"type": "arbitrary", "samples": waveforms[key+"_minus_y90_I"].tolist()} for key in QUBIT_CONSTANTS.keys()},
        **{f"minus_y90_Q_wf_{key}": {"type": "arbitrary", "samples": waveforms[key+"_minus_y90_Q"].tolist()} for key in QUBIT_CONSTANTS.keys()},
        **{f"readout_wf_{key}": {"type": "constant", "sample": RR_CONSTANTS[key]["amplitude"]} for key in RR_CONSTANTS.keys()},
        **{f"midcircuit_readout_wf_{key}": {"type": "constant", "sample": RR_CONSTANTS[key]["midcircuit_amplitude"]} for key in RR_CONSTANTS.keys()},
    },
    "digital_waveforms": {
        "ON": {"samples": [(1, 0)]},
    },
    "integration_weights": {
        "cosine_weights": {
            "cosine": [(1.0, readout_len)],
            "sine": [(0.0, readout_len)],
        },
        "sine_weights": {
            "cosine": [(0.0, readout_len)],
            "sine": [(1.0, readout_len)],
        },
        "minus_sine_weights": {
            "cosine": [(0.0, readout_len)],
            "sine": [(-1.0, readout_len)],
        },
        **{
            f"rotated_cosine_weights_{key}": {
                "cosine": [(np.cos(RR_CONSTANTS[key]["rotation_angle"])), readout_len],
                "sine": [(np.sin(RR_CONSTANTS[key]["rotation_angle"])), readout_len]
            } for key in RR_CONSTANTS.keys()
        },
        **{
            f"rotated_sine_weights_{key}": {
                "cosine": [(-np.sin(RR_CONSTANTS[key]["rotation_angle"])), readout_len],
                "sine": [(np.cos(RR_CONSTANTS[key]["rotation_angle"])), readout_len]
            } for key in RR_CONSTANTS.keys()
        },
        **{
            f"rotated_minus_sine_weights_{key}": {
                "cosine": [(np.sin(RR_CONSTANTS[key]["rotation_angle"])), readout_len],
                "sine": [(-np.cos(RR_CONSTANTS[key]["rotation_angle"])), readout_len]
            } for key in RR_CONSTANTS.keys()
        },
        **{
            f"opt_cosine_weights_{key}": {
                "cosine": OPT_WEIGHTS[key]['real'],
                "sine": OPT_WEIGHTS[key]['minus_imag']
            } for key in RR_CONSTANTS.keys()
        },
        **{
            f"opt_sine_weights_{key}": {
                "cosine": OPT_WEIGHTS[key]['imag'],
                "sine": OPT_WEIGHTS[key]['real']
            } for key in RR_CONSTANTS.keys()
        },
        **{
            f"opt_minus_sine_weights_{key}": {
                "cosine": OPT_WEIGHTS[key]['minus_imag'],
                "sine": OPT_WEIGHTS[key]['minus_real']
            } for key in RR_CONSTANTS.keys()
        },
        **{
            f"midcircuit_rotated_cosine_weights_{key}": {
                "cosine": [(np.cos(RR_CONSTANTS[key]["midcircuit_rotation_angle"])), readout_len],
                "sine": [(np.sin(RR_CONSTANTS[key]["midcircuit_rotation_angle"])), readout_len]
            } for key in RR_CONSTANTS.keys()
        },
        **{
            f"midcircuit_rotated_sine_weights_{key}": {
                "cosine": [(-np.sin(RR_CONSTANTS[key]["midcircuit_rotation_angle"])), readout_len],
                "sine": [(np.cos(RR_CONSTANTS[key]["midcircuit_rotation_angle"])), readout_len]
            } for key in RR_CONSTANTS.keys()
        },
        **{
            f"midcircuit_rotated_minus_sine_weights_{key}": {
                "cosine": [(np.sin(RR_CONSTANTS[key]["midcircuit_rotation_angle"])), readout_len],
                "sine": [(-np.cos(RR_CONSTANTS[key]["midcircuit_rotation_angle"])), readout_len]
            } for key in RR_CONSTANTS.keys()
        },
        **{
            f"midcircuit_opt_cosine_weights_{key}": {
                "cosine": OPT_WEIGHTS[key]['real'],
                "sine": OPT_WEIGHTS[key]['minus_imag']
            } for key in RR_CONSTANTS.keys()
        },
        **{
            f"midcircuit_opt_sine_weights_{key}": {
                "cosine": OPT_WEIGHTS[key]['imag'],
                "sine": OPT_WEIGHTS[key]['real']
            } for key in RR_CONSTANTS.keys()
        },
        **{
            f"midcircuit_opt_minus_sine_weights_{key}": {
                "cosine": OPT_WEIGHTS[key]['minus_imag'],
                "sine": OPT_WEIGHTS[key]['minus_real']
            } for key in RR_CONSTANTS.keys()
        },
    },
    "mixers": {},
    
}


# %%
