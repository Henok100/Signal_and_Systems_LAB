import numpy as np
import matplotlib.pyplot as plt

# Define the number of samples
N = 100  # Total number of samples
n = np.arange(0, N)  # Discrete time vector

# Create the original Periodic Signal: x[n] = sin(2πfn/N)
f_periodic = 5  # Frequency in Hz
x_periodic = np.sin(2 * np.pi * f_periodic * n / N)

# Create another Periodic Signal: x[n] = cos(2πfn/N)
f_periodic_2 = 3  # Different frequency in Hz
x_periodic_2 = np.cos(2 * np.pi * f_periodic_2 * n / N)

# Create a Non-Periodic Signal: Ramp Function
x_non_periodic = n  # Ramp function

# Plotting the results
plt.figure(figsize=(12, 10))

# Original Periodic Signal
plt.subplot(3, 1, 1)
plt.stem(n, x_periodic, label='Periodic Signal: $x[n] = \sin(2\pi f n / N)$', basefmt=" ", linefmt='blue', markerfmt='bo')
plt.title('Periodic Signal')
plt.xlabel('Sample n')
plt.ylabel('Amplitude')
plt.grid()
plt.legend()

# New Periodic Signal
plt.subplot(3, 1, 2)
plt.stem(n, x_periodic_2, label='Periodic Signal: $x[n] = \cos(2\pi f n / N)$', basefmt=" ", linefmt='orange', markerfmt='ro')
plt.title('Periodic Signal')
plt.xlabel('Sample n')
plt.ylabel('Amplitude')
plt.grid()
plt.legend()

# Non-Periodic Signal
plt.subplot(3, 1, 3)
plt.stem(n, x_non_periodic, label='Non-Periodic Signal: Ramp Function', basefmt=" ", linefmt='green', markerfmt='go')
plt.title('Non-Periodic Signal')
plt.xlabel('Sample n')
plt.ylabel('Amplitude')
plt.grid()
plt.legend()

plt.tight_layout()
plt.show()
