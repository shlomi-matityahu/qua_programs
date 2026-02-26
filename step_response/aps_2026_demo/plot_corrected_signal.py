# %%
import numpy as np
import matplotlib.pyplot as plt

# Larger fonts for all figures
plt.rcParams["axes.labelsize"] = 16
plt.rcParams["axes.titlesize"] = 18
plt.rcParams["xtick.labelsize"] = 14
plt.rcParams["ytick.labelsize"] = 14
plt.rcParams["legend.fontsize"] = 14

# %%
data = np.loadtxt("step_response_with_and_without_bias_tee_with_filters.csv", delimiter=",")

t_raw = data[:, 0] * 1e9 # convert to ns
y_raw_without_biastee = data[:, 1]
y_raw_with_biastee_corrected = data[:, 2]

plt.figure(figsize=(10, 6))
plt.plot(t_raw, y_raw_without_biastee, label="without bias tee")
plt.plot(t_raw, y_raw_with_biastee_corrected, label="with bias tee and filters")
plt.xlabel("Time [ns]")
plt.ylabel("Voltage [V]")
plt.title("Step response with and without bias tee - digital filters correction")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

mask_t1 = (t_raw > 0) & (t_raw < 1.2e3)
mask_v1 = y_raw_with_biastee_corrected > 0
mask = mask_t1 & mask_v1 

t_data = t_raw[mask]
y_data_without_biastee = y_raw_without_biastee[mask]
y_data_with_biastee_corrected = y_raw_with_biastee_corrected[mask]

plt.figure(figsize=(10, 6))
plt.semilogx(t_data, y_data_without_biastee, label="without bias tee")
plt.semilogx(t_data, y_data_with_biastee_corrected, label="with bias tee and filters")
plt.xlabel("Time [ns]")
plt.ylabel("Voltage [V]")
plt.title("Step response with and without bias tee - digital filters correction")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
# %%
