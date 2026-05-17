"""LO sweep program for the 18GHz testing
Two channels to to a 3-port mixer. 
"resonator1" is the "LO" port of the mixer.
"resonator2" is the "IF" port of the mixer.
The LO frequency or "resonator2" is swept from -7.5 GHz to 9.5 GHz in 100 MHz steps.
The program pauses at each frequency so that the user can read out the signal on a 
spectrum analyzer before proceeding to the next frequency.

To change the LO/IF/power/amplitude, see the configuration.py file.
"""

# %% Imports
from qm.qua import *
from qm import QuantumMachinesManager, SimulationConfig
from qualang_tools.units import unit
from configuration import *
import time

u = unit(coerce_to_integer=True)

# %% Define the QUA program
step_hz = int(100 * u.MHz)
delta_LO_values: list[int] = [i * step_hz for i in range(0, 1)]  # -1000 … +1000 MHz in 100 MHz steps

with program() as LO_sweep:
    freq = declare(int)

    play("cw", "resonator1_sticky") # the "LO" of the mixer
    with for_each_(freq, delta_LO_values):
        pause() # pause to update the LO frequency
        play("cw", "resonator2" \
        "_sticky") # the "IF" of the mixer
        pause() # pause to measure the signal on the spectrum analyzer
        ramp_to_zero("resonator2_sticky")
    ramp_to_zero("resonator1_sticky")


# %% Open communication with the OPX
qmm = QuantumMachinesManager(host=qop_ip, cluster_name=cluster_name)
qm = qmm.open_qm(config, close_other_machines=True)

# %% Execute the QUA program

simulate = False

if simulate:
    simulation_config = SimulationConfig(duration=10_000_000)  # clock cycles (4 ns each)
    job = qmm.simulate(config, LO_sweep, simulation_config)
else:
    job = qm.execute(LO_sweep)
    print(job.get_job_id())

    # One pause() per IF step; host must call resume() to reach the next frequency
    for i, freq in enumerate(delta_LO_values):
        while not job.is_paused():
            time.sleep(0.1)
        job.update_oscillator_frequency("resonator2_sticky", (freq + LO2), "both")
        job.resume()
        while not job.is_paused():
            time.sleep(0.1)
        print(f"Paused at F = {(LO2 + freq) / 1e9:.2f} GHz ({i + 1}/{len(delta_LO_values)})")
        input("Press Enter to proceed to the next frequency.")  
        job.resume()
    
    while not job.is_finished():
        time.sleep(0.1)
    print("Program completed.")