"""
QUA-Config supporting OPX1000 w/ MW-FEM
"""

from pathlib import Path

import numpy as np
from qualang_tools.units import unit
import plotly.io as pio

pio.renderers.default = "browser"

#######################
# AUXILIARY FUNCTIONS #
#######################
u = unit(coerce_to_integer=True)

######################
# Network parameters #
######################
qop_ip = "10.1.1.16"  # Write the QM router IP address
cluster_name = "4_OPXK4"  # Write your cluster_name if version >= QOP220

#############
# Save Path #
############
# Path to save data
save_dir = Path(__file__).parent.resolve() / "Data"
save_dir.mkdir(exist_ok=True)

#####################
# OPX configuration #
#####################

con = "con1"
fem = 1
LO_channel = 7 # The LO of the mixer
IF_channel = 8 # The IF of the mixer

# Band 3: 6.5 GHz – 10.5 GHz (MW-FEM). Choose LO/IF so RF lies in this band.
IF1 = 0 * u.MHz
IF2 = 0 * u.MHz
LO1 = 10.0 * u.GHz  # The "LO" of the mixer
LO2 = 8.5 * u.GHz   # The "IF" of the mixer

LO_power = 16  # dBm at waveform amp = 1 (3 dB steps)
IF_power = 5  # dBm at waveform amp = 1 (3 dB steps)

const_len = 100 * u.ns
const_amp = 1

time_of_flight = 28 * u.ns

# Sticky elements hold the last analog sample for this duration (ns) after each pulse.
sticky_duration = 20

#############################################
#                  Config                   #
#############################################
config = {
    "version": 1,
    "controllers": {
        con: {
            "type": "opx1000",
            "fems": {
                fem: {
                    # The keyword "band" refers to the following frequency bands:
                    #   1: (50 MHz - 5.5 GHz)
                    #   2: (4.5 GHz - 7.5 GHz)
                    #   3: (6.5 GHz - 10.5 GHz)
                    # Note that the "coupled" ports O1 & I1, O2 & O3, O4 & O5, O6 & O7, and O8 & I2
                    # must be in the same band, or in bands 1 & 3 (that is, if you assign band 2 to one of the coupled ports, the other must use the same band).
                    # The keyword "full_scale_power_dbm" is the maximum power of
                    # normalized pulse waveforms in [-1,1]. To convert to voltage,
                    #   power_mw = 10**(full_scale_power_dbm / 10)
                    #   max_voltage_amp = np.sqrt(2 * power_mw * 50 / 1000)
                    #   amp_in_volts = waveform * max_voltage_amp
                    #   ^ equivalent to OPX+ amp
                    # Its range is -41dBm to +10dBm with 3dBm steps.
                    "type": "MW",
                    "analog_outputs": {
                        LO_channel: {
                            "band": 3,
                            "full_scale_power_dbm": LO_power,
                            "upconverters": {1: {"frequency": LO1}},
                        },
                        IF_channel: {
                            "band": 3,
                            "full_scale_power_dbm": IF_power,
                            "upconverters": {1: {"frequency": LO2}},
                        },
                    },
                    "digital_outputs": {},
                    "analog_inputs": {
                        1: {"band": 3, "downconverter_frequency": LO1},
                        2: {"band": 3, "downconverter_frequency": LO2},
                    },
                },
            },
        },
    },
    "elements": {
        "resonator1": {
            "MWInput": {
                "port": (con, fem, LO_channel),
                "upconverter": 1,
            },
            "intermediate_frequency": IF1,
            "operations": {
                "cw": "const_pulse",
            },
            "MWOutput": {
                "port": (con, fem, 1),
            },
            "time_of_flight": time_of_flight,
            "smearing": 0,
        },
        "resonator2": {
            "MWInput": {
                "port": (con, fem, IF_channel),
                "upconverter": 1,
            },
            "intermediate_frequency": IF2,
            "operations": {
                "cw": "const_pulse",
            },
            "MWOutput": {
                "port": (con, fem, 2),
            },
            "time_of_flight": time_of_flight,
            "smearing": 0,
        },
        "resonator1_sticky": {
            "MWInput": {
                "port": (con, fem, LO_channel),
                "upconverter": 1,
            },
            "intermediate_frequency": IF1,
            "sticky": {"analog": True, "duration": sticky_duration},
            "operations": {
                "cw": "const_pulse",
            },
            "MWOutput": {
                "port": (con, fem, 1),
            },
            "time_of_flight": time_of_flight,
            "smearing": 0,
        },
        "resonator2_sticky": {
            "MWInput": {
                "port": (con, fem, IF_channel),
                "upconverter": 1,
            },
            "intermediate_frequency": IF2,
            "sticky": {"analog": True, "duration": sticky_duration},
            "operations": {
                "cw": "const_pulse",
            },
            "MWOutput": {
                "port": (con, fem, 2),
            },
            "time_of_flight": time_of_flight,
            "smearing": 0,
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
    },
    "waveforms": {
        "const_wf": {"type": "constant", "sample": const_amp},
        "zero_wf": {"type": "constant", "sample": 0.0},
    },
    "digital_waveforms": {
        "ON": {"samples": [(1, 0)]},
    },
    "integration_weights": {
        "cosine_weights": {
            "cosine": [(1.0, const_len)],
            "sine": [(0.0, const_len)],
        },
        "sine_weights": {
            "cosine": [(0.0, const_len)],
            "sine": [(1.0, const_len)],
        },
    },
}
