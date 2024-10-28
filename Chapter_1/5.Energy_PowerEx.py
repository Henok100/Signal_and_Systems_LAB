import numpy as np
import matplotlib.pyplot as plt

# Define the time vector for both signals
# We're setting a larger time range for clarity in observing the signals
t = np.linspace(-5, 5, 1000)

### 1. Rectangular Pulse (Energy Signal) ###

# Define parameters for the rectangular pulse
A_pulse = 2  # Amplitude of the pulse
width_pulse = 2  # Width of the pulse in time units

# Generate the rectangular pulse signal
# Using numpy's where function to set the pulse value within the width and zero outside
x_energy = A_pulse * np.where(abs(t) <= width_pulse / 2, 1, 0)

# Calculate the energy of the rectangular pulse
# Using numerical integration with np.trapz to approximate the integral of |x(t)|^2 over time
energy_rect_pulse = np.trapz(x_energy ** 2, t)

### 2. Square Wave (Power Signal) ###

# Define parameters for the square wave
f_square = 0.5  # Frequency in Hz (controls the period)
A_square = 1  # Amplitude of the square wave

# Generate the square wave signal
# The square wave alternates between +A_square and -A_square periodically
x_power = A_square * np.sign(np.sin(2 * np.pi * f_square * t))

# Calculate the average power of the square wave
# We approximate the average power over a large interval to represent infinite time
power_square_wave = np.trapz(x_power ** 2, t) / (t[-1] - t[0])

### Plotting both signals ###

plt.figure(figsize=(12, 6))

# Plot Rectangular Pulse (Energy Signal)
plt.subplot(2, 1, 1)
plt.plot(t, x_energy, label=f'Rectangular Pulse (Energy = {energy_rect_pulse:.2f})', color='blue')
plt.title("Energy Signal: Rectangular Pulse")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.legend()

# Plot Square Wave (Power Signal)
plt.subplot(2, 1, 2)
plt.plot(t, x_power, label=f'Square Wave (Power = {power_square_wave:.2f})', color='orange')
plt.title("Power Signal: Square Wave")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.legend()

# Adjust layout for better display
plt.tight_layout()
plt.show()