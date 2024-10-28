import numpy as np
import matplotlib.pyplot as plt

# Define the time vector
t = np.linspace(-2 * np.pi, 2 * np.pi, 1000)  # Time from -2π to 2π

# Generate the original signal x(t) = sin(t) + cos(t)
x_t = np.sin(t) + np.cos(t)

# Calculate the even part x_e(t)
x_e = 0.5 * (x_t + np.flip(x_t))  # x(-t) is achieved by flipping the signal

# Calculate the odd part x_o(t)
x_o = 0.5 * (x_t - np.flip(x_t))

# Plotting the results
plt.figure(figsize=(12, 8))

# Original Signal
plt.subplot(3, 1, 1)
plt.plot(t, x_t, label='Original Signal: $x(t) = \sin(t) + \cos(t)$', color='blue')
plt.title('Original Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid()
plt.legend()

# Even Part
plt.subplot(3, 1, 2)
plt.plot(t, x_e, label='Even Part: $x_e(t)$', color='orange')
plt.title('Even Part of the Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid()
plt.legend()

# Odd Part
plt.subplot(3, 1, 3)
plt.plot(t, x_o, label='Odd Part: $x_o(t)$', color='green')
plt.title('Odd Part of the Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid()
plt.legend()

plt.tight_layout()
plt.show()