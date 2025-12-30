
# %%
import os
os.chdir("/home/shlomimatit/Projects/hardware_measurements/qua_programs/intel")

from qm import QuantumMachinesManager, SimulationConfig
from qua_config import *
from qm.qua import *

# %%
OPX_IP = "10.1.1.18"
qmm = QuantumMachinesManager(host=OPX_IP, cluster_name="galil_meron")

# %%
qm = qmm.open_qm(config, close_other_machines=True)

# %%

amplitudes = np.random.uniform(0.9, 1.0, size=1000)
print(amplitudes)

with program() as qua_program:
    amp_array = declare(fixed, value=amplitudes.tolist())
    r = Random()
    for i in range(1, 65):
        j = declare(int)
        with infinite_loop_():
            play(element=f"qubit{i}", pulse="cw")
            with for_(j, 0, j < 1000, j + 1):
                play(element=f"qubit{i}", pulse="cw"*amp(0.5*amp_array[j]), duration=2)          
                play(element=f"qubit{i}", pulse="cw"*amp(-0.25*amp_array[j]), duration=5)     

# with program() as qua_program:
#     for i in range(1, 65):
#         with infinite_loop_():
#             play(element=f"qubit{i}", pulse="cw"*amp(0.5), duration=2)          
#             play(element=f"qubit{i}", pulse="cw"*amp(-0.25), duration=5)

job = qm.execute(qua_program)

# %%
simulated_job = qmm.simulate(
    config,
    qua_program,
    SimulationConfig(
        duration=150,  # duration of simulation in units of 4ns
    ),
)

samples = simulated_job.get_simulated_samples()
samples.con1.plot()

res = simulated_job.result_handles
c = res.c.fetch_all()
print(c)
 # %%
# qm.close()

# %%
