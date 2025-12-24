import numpy as np
from scipy.signal.windows import gaussian
from qm.qua import *
from qm import DictQuaConfig


#######################
# AUXILIARY FUNCTIONS #
#######################

# IQ imbalance matrix
def IQ_imbalance(g, phi):
    c = np.cos(phi)
    s = np.sin(phi)
    N = 1 / ((1 - g ** 2) * (2 * c ** 2 - 1))
    return [float(N * x) for x in [(1 - g) * c, (1 + g) * s, (1 - g) * s, (1 + g) * c]]


#############ff
# VARIABLES #
#############

# Qubits
qubit1_IF = 0.0
qubit2_IF = 0.0
qubit3_IF = 0.0
resonator_IF = 74e6
resonator_LO = 7e9

const_len = 100
# const_amp = 0.4
const_amp = 2.5

gauss_len = 20

sqrt_amp = 0.2
gauss_sigma = gauss_len / 5
gauss_amp = 0.45
gauss_wf = gauss_amp * gaussian(gauss_len, gauss_sigma)
sqrt_wf = np.sqrt(np.linspace(0, sqrt_amp, const_len))

readout_len = 500
readout_amp = 0.2
long_readout_len = 50000
timetagging_len = 3800
phase_coherence_pulse = 250

# Complex chirping
chirp_len = 4000
freq = 50e5
theta = 0.1
t = np.arange(-50, 51, 1)
freq_vec = [freq * np.tanh(theta * t)]
freq_1D = np.concatenate(np.array(freq_vec)).astype(int).tolist()
chirp_vec = [np.diff(freq * np.sin(theta * t))]
chirp_1D = np.concatenate(np.array(chirp_vec) / chirp_len).astype(int).tolist()

##########
# CONFIG #
##########
config: DictQuaConfig = {
    "version": 1,
    "controllers": {
        "con1": {
            "type": "opx1000",
            "fems": {
                6: {  # LF-FEM
                    "type": "LF",
                    "analog_outputs": {
                        1: {"offset": 0.0,'output_mode':'amplified'},
                        2: {"offset": 0.0,'output_mode':'amplified'},
                        3: {"offset": 0.0, 'output_mode':'amplified', 'sampling_rate': 2e9, 'filter': {'feedforward': [
                            0.36407847281072603,
                            0.4901759397435047,
                            0.28493246664269106,
                            0.07801292603398545,
                            -0.014407382083091145,
                            -0.04079046815785396,
                            -0.04352093511033222,
                            -0.035689207026010646,
                            -0.023079429436846353,
                            -0.011282891044654807,
                            -0.0037838131287710247,
                        ]}},
                        4: {"offset": 0.0},
                        5: {"offset": 0.0,'output_mode':'amplified'},
                        6: {"offset": 0.0},
                        7: {"offset": 0.0,'output_mode':'amplified'},
                        8: {"offset": 0.0,'output_mode':'amplified'},
                    },
                    "analog_inputs": {
                        1: {"offset": 0.0, "gain_db": 0},
                    },
                    "digital_outputs": {1: {}, 2: {}, 3: {}, 4: {}, 5: {}, 6: {}, 7: {}},
                },
            }
        },
    },
    "elements": {
        "qubit1": {
            "singleInput": {
                "port": ("con1", 6, 3),
            },
            "intermediate_frequency": qubit1_IF,
            "operations": {
                "cw": "const_pulse_single",
            },
        },
        "qubit2": {
            "singleInput": {
                "port": ("con1", 6, 3),
            },
            "intermediate_frequency": qubit1_IF,
            "operations": {
                "cw": "const_pulse_single",
            },
        },
        "qubit3": {
            "singleInput": {
                "port": ("con1", 6, 3),
            },
            "intermediate_frequency": qubit1_IF,
            "operations": {
                "cw": "const_pulse_single",
            },
        },
      
     
    },
    "pulses": {
        "const_pulse": {
            "operation": "control",
            "length": const_len,
            "waveforms": {
                "I": "const_wf",
                "Q": "zero_wf",
            },
        },
        "const_pulse_single": {
            "operation": "control",
            "length": const_len,
            "waveforms": {
                "single": "const_wf",
            },
        },
        "sqrt_pulse": {
            "operation": "control",
            "length": const_len,
            "waveforms": {
                "I": "sqrt_wf",
                "Q": "zero_wf",
            },
        },
        "sqrt_pulse_single": {
            "operation": "control",
            "length": const_len,
            "waveforms": {
                "single": "sqrt_wf",
            },
        },
        "long_pulse": {
            "operation": "control",
            "length": 2 * long_readout_len,
            "waveforms": {
                "I": "const_wf",
                "Q": "zero_wf",
            },
        },
        "long_pulse_single": {
            "operation": "control",
            "length": 2 * long_readout_len,
            "waveforms": {
                "single": "const_wf",
            },
        },
        "gaussian_pulse": {
            "operation": "control",
            "length": gauss_len,
            "waveforms": {
                "I": "gauss_wf",
                "Q": "zero_wf",
            },
        },
        "gaussian_pulse_single": {
            "operation": "control",
            "length": gauss_len,
            "waveforms": {
                "single": "gauss_wf",
            },
        },
        "readout_pulse": {
            "operation": "measurement",
            "length": readout_len,
            "waveforms": {
                "I": "readout_wf",
                "Q": "zero_wf",
            },
            "integration_weights": {
                "cos": "cosine_weights",
                "sin": "sine_weights",
            },
            "digital_marker": "ON",
        },
        "readout_pulse_single": {
            "operation": "measurement",
            "length": readout_len,
            "waveforms": {
                "single": "readout_wf",
            },
            "integration_weights": {
                "cos": "cosine_weights",
                "sin": "sine_weights",
            },
            "digital_marker": "ON",
        },
        "readout_pulse_timetagging": {
            "operation": "measurement",
            "length": timetagging_len,
            "waveforms": {
                "single": "zero_wf",
            },
            "digital_marker": "ON",
        },
    },
    "waveforms": {
        "const_wf": {"type": "constant", "sample": const_amp},
        "sqrt_wf": {"type": "arbitrary", "samples": sqrt_wf.tolist()},
        "zero_wf": {"type": "constant", "sample": 0.0},
        "gauss_wf": {"type": "arbitrary", "samples": gauss_wf.tolist()},
        "readout_wf": {"type": "constant", "sample": readout_amp},
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
    },
}


