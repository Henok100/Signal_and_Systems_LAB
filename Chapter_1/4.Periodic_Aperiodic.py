import numpy as np
import matplotlib.pyplot as plt

# Define the time vector for the periodic signal
t_periodic = np.linspace(0, 1, 1000)  # Time from 0 to 1 second
f = 5  # Frequency in Hz
# Generate the periodic signal x(t) = sin(2πft)
x_periodic = np.sin(2 * np.pi * f * t_periodic)

# Define the time vector for the non-periodic signal
t_non_periodic = np.linspace(0, 5, 1000)  # Time from 0 to 5 seconds
# Generate a non-periodic ramp signal
x_non_periodic = t_non_periodic  # Ramp function

# Plotting the results
plt.figure(figsize=(12, 8))

# Periodic Signal
plt.subplot(2, 1, 1)
plt.plot(t_periodic, x_periodic, label='Periodic Signal: $x(t) = \sin(2\pi ft)$', color='blue')
plt.title('Periodic Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid()
plt.legend()


# Non-Periodic Signal
plt.subplot(2, 1, 2)
plt.plot(t_non_periodic, x_non_periodic, label='Non-Periodic Signal: Ramp Function', color='orange')
plt.title('Non-Periodic Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid()
plt.legend()


plt.tight_layout()
plt.show()