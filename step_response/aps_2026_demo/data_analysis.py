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
square_pulse_3m_vs_12m = np.loadtxt("Square_pulse_3m_vs_12m.csv", delimiter=",")
square_pulse_3m_vs_12m_with20dB = np.loadtxt("Square_pulse_3m_vs_12m_with20dB.csv", delimiter=",")
square_pulse_3m_vs_12m_with20dB_ir_lpf = np.loadtxt("Square_pulse_3m_vs_12m_with20dB-ir-lpf.csv", delimiter=",")
square_pulse_3m_vs_12m_with20dB_ir_lpf_biast = np.loadtxt("Square_pulse_3m_vs_12m_with20dB-ir-lpf-biast.csv", delimiter=",")

# %%
plt.figure(figsize=(10, 6))
square_pulse_3m_vs_12m[:, 0] += 2e-9
mask_t1 = (square_pulse_3m_vs_12m[:, 0] > 0) & (square_pulse_3m_vs_12m[:, 0] < 8e-8)
mask_v1 = square_pulse_3m_vs_12m[:, 1] > 0
mask = mask_t1 & mask_v1  # only positive x and y
plt.semilogx(square_pulse_3m_vs_12m[mask, 0], square_pulse_3m_vs_12m[mask, 1], label="3m")
plt.semilogx(square_pulse_3m_vs_12m[mask, 0], square_pulse_3m_vs_12m[mask, 2], label="12m")
plt.xlabel("Time [ns]")
plt.ylabel("Voltage [V]")
plt.title("Step response of the 3m vs 12m")
plt.grid(which="both")
plt.legend()
plt.tight_layout()
plt.show()

# %%
plt.figure(figsize=(10, 6))
square_pulse_3m_vs_12m_with20dB[:, 0] += 2e-9
mask_t1 = (square_pulse_3m_vs_12m_with20dB[:, 0] > 0) & (square_pulse_3m_vs_12m_with20dB[:, 0] < 8e-8)
mask_v1 = square_pulse_3m_vs_12m_with20dB[:, 1] > 0
mask = mask_t1 & mask_v1  # only positive x and y
plt.semilogx(square_pulse_3m_vs_12m_with20dB[mask, 0], square_pulse_3m_vs_12m_with20dB[mask, 1], label="3m")
plt.semilogx(square_pulse_3m_vs_12m_with20dB[mask, 0], 10 * square_pulse_3m_vs_12m_with20dB[mask, 2], label="12m with 20dB (multiplied by 10)")
plt.xlabel("Time [ns]")
plt.ylabel("Voltage [V]")
plt.title("Step response of the 3m vs 12m with 20dB")
plt.grid(which="both")
plt.legend()
plt.tight_layout()
plt.show()
# %%
plt.figure(figsize=(10, 6))
square_pulse_3m_vs_12m_with20dB_ir_lpf[:, 0] += 2e-9
mask_t1 = (square_pulse_3m_vs_12m_with20dB_ir_lpf[:, 0] > 0) & (square_pulse_3m_vs_12m_with20dB_ir_lpf[:, 0] < 8e-8)
mask_v1 = square_pulse_3m_vs_12m_with20dB_ir_lpf[:, 1] > 0
mask = mask_t1 & mask_v1  # only positive x and y
plt.semilogx(square_pulse_3m_vs_12m_with20dB_ir_lpf[mask, 0], square_pulse_3m_vs_12m_with20dB_ir_lpf[mask, 1], label="3m")
plt.semilogx(square_pulse_3m_vs_12m_with20dB_ir_lpf[mask, 0], 10 * square_pulse_3m_vs_12m_with20dB_ir_lpf[mask, 2], label="12m with 20dB + IR + LPF (multiplied by 10)")
plt.xlabel("Time [ns]")
plt.ylabel("Voltage [V]")
plt.title("Step response of the 3m vs 12m with 20dB + IR + LPF")
plt.grid(which="both")
plt.legend()
plt.tight_layout()
plt.show()

# %%
plt.figure(figsize=(10, 6))
square_pulse_3m_vs_12m_with20dB_ir_lpf_biast[:, 2] += 0.04  # add 40mV to the 12m signal
square_pulse_3m_vs_12m_with20dB_ir_lpf_biast[:, 0] += 2e-9
mask_t1 = (square_pulse_3m_vs_12m_with20dB_ir_lpf_biast[:, 0] > 0) & (square_pulse_3m_vs_12m_with20dB_ir_lpf_biast[:, 0] < 8e-8)
mask_v1 = square_pulse_3m_vs_12m_with20dB_ir_lpf_biast[:, 1] > 0
mask = mask_t1 & mask_v1  # only positive x and y
plt.semilogx(square_pulse_3m_vs_12m_with20dB_ir_lpf_biast[mask, 0], square_pulse_3m_vs_12m_with20dB_ir_lpf_biast[mask, 1], label="3m")
plt.semilogx(square_pulse_3m_vs_12m_with20dB_ir_lpf_biast[mask, 0], 10 * square_pulse_3m_vs_12m_with20dB_ir_lpf_biast[mask, 2], label="12m with 20dB + IR + LPF (multiplied by 10)")
plt.xlabel("Time [ns]")
plt.ylabel("Voltage [V]")
plt.title("Step response of the 3m vs 12m with 20dB + IR + LPF + bias tee")
plt.grid(which="both")
plt.legend()
plt.tight_layout()
plt.show()
# %%
