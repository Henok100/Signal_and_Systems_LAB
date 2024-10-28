import numpy as np
import matplotlib.pyplot as plt

# Time vector for both signals
t = np.linspace(-5, 5, 1000)

# 1. Gaussian Pulse (Energy Signal)
A = 1    # Amplitude
sigma = 0.5  # Width of the Gaussian
x_energy = A * np.exp(-t**2 / (2 * sigma**2))

# Calculate the energy of the Gaussian pulse
energy_gaussian = np.trapz(x_energy**2, t)  # Numerical integration to find energy

# 2. Sine Wave (Power Signal)
f = 1  # Frequency in Hz
x_power = np.sin(2 * np.pi * f * t)

# Calculate the average power of the sine wave over a period
T = 1 / f  # Period of the sine wave
power_sine = np.trapz(x_power**2, t) / (t[-1] - t[0])  # Average power over time window

# Plot both signals
plt.figure(figsize=(12, 6))

# Plot Gaussian pulse (Energy Signal)
plt.subplot(2, 1, 1)
plt.plot(t, x_energy, label=f'Gaussian Pulse (Energy = {energy_gaussian:.2f})')
plt.title("Energy Signal: Gaussian Pulse")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.legend()

# Plot Sine wave (Power Signal)
plt.subplot(2, 1, 2)
plt.plot(t, x_power, label=f'Sine Wave (Power = {power_sine:.2f})')
plt.title("Power Signal: Sine Wave")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.legend()

plt.tight_layout()
plt.show()