"""Program with periodic pulses on the IF port of the mixer.
100ns pulses with 500ns repetition period.
The duration of the pulse can be changed in the configuration.py file.
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
LO_values: list[int] = [i * step_hz for i in range(-10, 11)]  # -1000 … +1000 MHz in 100 MHz steps

with program() as LO_sweep:
    freq = declare(int)

    play("cw", "resonator1_sticky") # the "LO" of the mixer
    with infinite_loop_():
        play("cw", "resonator2", duration=2*u.us) # the "IF" of the mixer (100ns pulse)
        wait(8*u.us)
    
    ramp_to_zero("resonator2_sticky")


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
    print(f"Job is running: {job.is_running()}")
    input("Press Enter to end the job.")
    job.cancel()
    while not job.is_finished():
        time.sleep(0.1)
    print("Program completed.")

