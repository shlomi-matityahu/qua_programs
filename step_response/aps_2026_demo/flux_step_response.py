
# %%
import os
os.chdir("/home/shlomimatit/Projects/hardware_measurements/qua_programs/step_response/aps_2026_demo")
from qm import QuantumMachinesManager
from lffem_configuration import *
from qm.qua import *

# %%
OPX_IP = "10.1.1.16"
qmm = QuantumMachinesManager(host=OPX_IP, cluster_name="4_OPXK4") 

# %%
qm = qmm.open_qm(config, close_other_machines=True)

# %%
with program() as prog1:
    with infinite_loop_():
        play(element="qubit1", pulse="cw", duration=3000)
        play(element="qubit3", pulse="cw", duration=3000)
        wait(3000)
 
job = qm.execute(prog1)

 # %%
# qm.close()
# %%
