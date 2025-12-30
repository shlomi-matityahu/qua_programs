import numpy as np
from scipy.signal.windows import gaussian
from qm.qua import *
from qm import DictQuaConfig


#############ff
# VARIABLES #
#############

# Qubits
qubit_IF = 0.0

const_len = 100
const_amp = 2.4

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
                1: {
                    "type": "LF",
                    "analog_outputs": {
                        1: {"offset": 0.0, 'output_mode': 'amplified'},
                        2: {"offset": 0.0, 'output_mode': 'amplified'},
                        3: {"offset": 0.0, 'output_mode': 'amplified'},
                        4: {"offset": 0.0, 'output_mode': 'amplified'},
                        5: {"offset": 0.0, 'output_mode': 'amplified'},
                        6: {"offset": 0.0, 'output_mode': 'amplified'},
                        7: {"offset": 0.0, 'output_mode': 'amplified'},
                        8: {"offset": 0.0, 'output_mode': 'amplified'},
                        },
                    },
                2: {
                    "type": "LF",
                    "analog_outputs": {
                        1: {"offset": 0.0, 'output_mode': 'amplified'},
                        2: {"offset": 0.0, 'output_mode': 'amplified'},
                        3: {"offset": 0.0, 'output_mode': 'amplified'},
                        4: {"offset": 0.0, 'output_mode': 'amplified'},
                        5: {"offset": 0.0, 'output_mode': 'amplified'},
                        6: {"offset": 0.0, 'output_mode': 'amplified'},
                        7: {"offset": 0.0, 'output_mode': 'amplified'},
                        8: {"offset": 0.0, 'output_mode': 'amplified'},
                        },
                    },
                3: {
                    "type": "LF",
                    "analog_outputs": {
                        1: {"offset": 0.0, 'output_mode': 'amplified'},
                        2: {"offset": 0.0, 'output_mode': 'amplified'},
                        3: {"offset": 0.0, 'output_mode': 'amplified'},
                        4: {"offset": 0.0, 'output_mode': 'amplified'},
                        5: {"offset": 0.0, 'output_mode': 'amplified'},
                        6: {"offset": 0.0, 'output_mode': 'amplified'},
                        7: {"offset": 0.0, 'output_mode': 'amplified'},
                        8: {"offset": 0.0, 'output_mode': 'amplified'},
                        },
                    },
                4: {
                    "type": "LF",
                    "analog_outputs": {
                        1: {"offset": 0.0, 'output_mode': 'amplified'},
                        2: {"offset": 0.0, 'output_mode': 'amplified'},
                        3: {"offset": 0.0, 'output_mode': 'amplified'},
                        4: {"offset": 0.0, 'output_mode': 'amplified'},
                        5: {"offset": 0.0, 'output_mode': 'amplified'},
                        6: {"offset": 0.0, 'output_mode': 'amplified'},
                        7: {"offset": 0.0, 'output_mode': 'amplified'},
                        8: {"offset": 0.0, 'output_mode': 'amplified'},
                        },
                    },
                5: {
                    "type": "LF",
                    "analog_outputs": {
                        1: {"offset": 0.0, 'output_mode': 'amplified'},
                        2: {"offset": 0.0, 'output_mode': 'amplified'},
                        3: {"offset": 0.0, 'output_mode': 'amplified'},
                        4: {"offset": 0.0, 'output_mode': 'amplified'},
                        5: {"offset": 0.0, 'output_mode': 'amplified'},
                        6: {"offset": 0.0, 'output_mode': 'amplified'},
                        7: {"offset": 0.0, 'output_mode': 'amplified'},
                        8: {"offset": 0.0, 'output_mode': 'amplified'},
                        },
                    },
                6: {
                    "type": "LF",
                    "analog_outputs": {
                        1: {"offset": 0.0, 'output_mode': 'amplified'},
                        2: {"offset": 0.0, 'output_mode': 'amplified'},
                        3: {"offset": 0.0, 'output_mode': 'amplified'},
                        4: {"offset": 0.0, 'output_mode': 'amplified'},
                        5: {"offset": 0.0, 'output_mode': 'amplified'},
                        6: {"offset": 0.0, 'output_mode': 'amplified'},
                        7: {"offset": 0.0, 'output_mode': 'amplified'},
                        8: {"offset": 0.0, 'output_mode': 'amplified'},
                        },
                    },
                7: {
                    "type": "LF",
                    "analog_outputs": {
                        1: {"offset": 0.0, 'output_mode': 'amplified'},
                        2: {"offset": 0.0, 'output_mode': 'amplified'},
                        3: {"offset": 0.0, 'output_mode': 'amplified'},
                        4: {"offset": 0.0, 'output_mode': 'amplified'},
                        5: {"offset": 0.0, 'output_mode': 'amplified'},
                        6: {"offset": 0.0, 'output_mode': 'amplified'},
                        7: {"offset": 0.0, 'output_mode': 'amplified'},
                        8: {"offset": 0.0, 'output_mode': 'amplified'},
                        },
                    },
                8: {
                    "type": "LF",
                    "analog_outputs": {
                        1: {"offset": 0.0, 'output_mode': 'amplified'},
                        2: {"offset": 0.0, 'output_mode': 'amplified'},
                        3: {"offset": 0.0, 'output_mode': 'amplified'},
                        4: {"offset": 0.0, 'output_mode': 'amplified'},
                        5: {"offset": 0.0, 'output_mode': 'amplified'},
                        6: {"offset": 0.0, 'output_mode': 'amplified'},
                        7: {"offset": 0.0, 'output_mode': 'amplified'},
                        8: {"offset": 0.0, 'output_mode': 'amplified'},
                        },
                    },
                },
            },
        },
    "elements": {
        **{f"qubit{(i-1)*8 + j}": {
            "singleInput": {
                "port": ("con1", i, j),
            },
            "intermediate_frequency": qubit_IF,
            "operations": {
                "cw": "const_pulse_single",
            },
        } 
        for i in range(1, 9) for j in range(1, 9)}
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


