# %% imports
import numpy as np
import matplotlib.pyplot as plt

# %%
# Load the CSV file LF_step_response_2GSPS.csv
data = np.loadtxt('LF_step_response_single_cw_2p5V_2GSPS_50ohm.csv', delimiter=',')
time = data[:, 0]
voltage = data[:, 1]
# voltage = voltage / voltage[-50:].mean()

# %%
# Find the index where the step starts (largest upward voltage jump)
step_diff = np.diff(voltage)
step_start_idx = np.argmax(step_diff) - 300
voltage = voltage[step_start_idx:-150]
time = time[step_start_idx:-150]

#%%
def downsample_signal(signal, time, factor):
    return signal[::factor], time[::factor]

def calculate_rise_time(signal, time):
    v_min = np.min(signal)
    v_max = np.max(signal)
    v_10 = v_min + 0.1 * (v_max - v_min)
    v_90 = v_min + 0.9 * (v_max - v_min)

    idx_10 = np.where(signal >= v_10)[0][0]
    idx_90 = np.where(signal >= v_90)[0][0]

    t_10 = time[idx_10]
    t_90 = time[idx_90]
    rise_time = t_90 - t_10
    return rise_time, t_10, t_90

rise_time, t_10, t_90 = calculate_rise_time(voltage, time)
downsampling_factor = int(round(0.5e-9 / np.mean(np.diff(time))))
voltage_downsampled, time_downsampled = downsample_signal(voltage, time, downsampling_factor)
rise_time_downsampled, t_10_downsampled, t_90_downsampled = calculate_rise_time(voltage_downsampled, time_downsampled)
print(f'Rise time (10% to 90%): {rise_time*1e9:.2f} ns')
print(f'Rise time (10% to 90%) of downsampled signal: {rise_time_downsampled*1e9:.2f} ns')
print(f'Downsampling factor: {downsampling_factor}')

# %%
plt.figure(figsize=(10, 6))
plt.plot(time * 1e9, voltage, label="Voltage")
plt.axvline(t_10 * 1e9, color='red', linestyle='--', label='10%')
plt.axvline(t_90 * 1e9, color='green', linestyle='--', label='90%')
# Plot the rise time as an arrow
plt.annotate(
    "",
    xy=(t_90 * 1e9, voltage.min()), 
    xytext=(t_10 * 1e9, voltage.min()),
    arrowprops=dict(arrowstyle="<->", color="blue", lw=2),
    annotation_clip=False,
)
plt.text(
    (t_10 + t_90) / 2 * 1e9,
    voltage.min() - 0.02 * (voltage.max()-voltage.min()),
    f"Rise time = {rise_time*1e9:.2f} ns",
    color="blue",
    ha="center",
    va="top"
)
plt.xlabel("Time [ns]")
plt.ylabel("Voltage [V]")
plt.title(r"Step response from 0V to +2.5V with 50$\Omega$ impedance")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# %%
normalized_voltage = voltage / voltage[-50:].mean()
normalized_voltage_downsampled, time_downsampled = downsample_signal(normalized_voltage, time, downsampling_factor)
plt.scatter(time_downsampled[4:] * 1e9, normalized_voltage_downsampled[4:], label="Normalized voltage")
plt.xlabel("Time [ns]")
plt.ylabel("Normalized voltage")
plt.title(r"Downsampled normalized step response from 0V to +2.5V with 50$\Omega$ impedance")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
