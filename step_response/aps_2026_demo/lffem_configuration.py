import numpy as np
from scipy.signal.windows import gaussian
from qm.qua import *
from qm import DictQuaConfig


#############
# VARIABLES #
#############

# Qubits
qubit1_IF = 0.0

const_len = 100
const_amp = 1.0

gauss_len = 20
gauss_sigma = gauss_len / 5
gauss_amp = 0.45
gauss_wf = gauss_amp * gaussian(gauss_len, gauss_sigma)

sqrt_amp = 0.2
sqrt_wf = np.sqrt(np.linspace(0, sqrt_amp, const_len))

##########
# CONFIG #
##########
config: DictQuaConfig = {
    "version": 1,
    "controllers": {
        "con1": {
            "type": "opx1000",
            "fems": {
                5: {
                    "type": "LF",
                    "analog_outputs": {
                        1: {"offset": 0.0, 'output_mode':'amplified'},
                        2: {"offset": 0.0, 'output_mode':'amplified', 'filter': {'exponential': [(0.982, 1403)], 'exponential_dc_gain': 0.01}},
                        3: {"offset": 0.0, 'output_mode':'amplified'},
                        4: {"offset": 0.0, 'output_mode':'amplified', 'filter': {'exponential': [(0.982, 1403)], 'exponential_dc_gain': 0.01}}
                    },
                },
            }
        },
    },
    "elements": {
        "qubit1": {
            "singleInput": {
                "port": ("con1", 5, 1),
            },
            "intermediate_frequency": qubit1_IF,
            "operations": {
                "cw": "const_pulse_single",
            },
        },
        "qubit2": {
            "singleInput": {
                "port": ("con1", 5, 2),
            },
            "intermediate_frequency": qubit1_IF,
            "operations": {
                "cw": "const_pulse_single",
            },
        },
        "qubit3": {
            "singleInput": {
                "port": ("con1", 5, 3),
            },
            "intermediate_frequency": qubit1_IF,
            "operations": {
                "cw": "const_pulse_single",
            },
        },
        "qubit4": {
            "singleInput": {
                "port": ("con1", 5, 4),
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
    },
    "waveforms": {
        "const_wf": {"type": "constant", "sample": const_amp},
        "sqrt_wf": {"type": "arbitrary", "samples": sqrt_wf.tolist()},
        "zero_wf": {"type": "constant", "sample": 0.0},
        "gauss_wf": {"type": "arbitrary", "samples": gauss_wf.tolist()},
    },
}
