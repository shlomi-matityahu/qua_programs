# %% imports
import numpy as np
import matplotlib
matplotlib.use('TkAgg')  # Use TkAgg backend for interactive window
import matplotlib.pyplot as plt
import os
import mplcursors

# %% load data
os.chdir("/home/shlomimatit/Projects/hardware_measurements/step_response/with_filters")
data = np.loadtxt('LF_step_response_2GSPS_with_filters.csv', delimiter=',')
time = data[:, 0]
voltage = data[:, 1]

# %% plot data
time_slice = time[1800:-3500] * 1e9
voltage_slice = voltage[1800:-3500]

fig, ax = plt.subplots(figsize=(10, 6))
line = ax.plot(time_slice, voltage_slice)
ax.set_xlabel('Time [ns]')
ax.set_ylabel('Voltage [V]')
ax.set_title('Step response with filters')
ax.grid(True)

# Enable hover tooltips
cursor = mplcursors.cursor(line, hover=False)
cursor.connect("add", lambda sel: sel.annotation.set_text(
    f'Time: {sel.target[0]:.2f} ns\nVoltage: {sel.target[1]:.4f} V'
))

plt.tight_layout()
plt.show(block=True)  # Block until window is closed
# %%