
# %%
import os
os.chdir("/home/shlomimatit/Projects/hardware_measurements/step_response")
# %%
from qm import QuantumMachinesManager
from lffem_configuration import *
from qm.qua import *

# %%
OPX_IP = "10.1.1.11"



qmm = QuantumMachinesManager(host=OPX_IP, cluster_name="carmel_gilboa")

# %%


# %%
qm = qmm.open_qm(config, close_other_machines=True)


# %%
with program() as prog1:
    update_frequency('qubit1', 0.0)
    set_dc_offset('qubit1','single', -2.5)
    x=declare(fixed)
    with infinite_loop_():
        # play(element="qubit3",pulse="cw"*amp(-1.0),duration=20)
        # align()
        # play(element="qubit2",pulse="cw"*amp(0.5),duration=20)
        play(element="qubit1", pulse="cw"*amp(0.5), duration=20)
        wait(20)
        #play(element="qubit1",pulse="cw"*amp(-1.0),duration=50000)

 

job = qm.execute(prog1)

 # %%
# qm.close()
# %%
