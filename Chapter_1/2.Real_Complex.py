import numpy as np
import matplotlib.pyplot as plt

# Set parameters for the signals
frequency = 1  # Frequency of the sine wave
sampling_rate = 100  # Sampling rate in Hz
duration = 2  # Duration in seconds

# Time vector
t = np.linspace(0, duration, sampling_rate * duration, endpoint=False)

# Generate a real signal (sine wave)
real_signal = np.sin(2 * np.pi * frequency * t)

# Generate a complex signal (e.g., e^(jωt))
complex_signal = np.exp(1j * 2 * np.pi * frequency * t)

# Plotting the signals
plt.figure(figsize=(12, 6))

# Plot real signal
plt.subplot(2, 1, 1)
plt.plot(t, real_signal, label='Real Signal (Sine Wave)', color='b')
plt.title('Real Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid()
plt.legend()

# Plot complex signal (real and imaginary parts)
plt.subplot(2, 1, 2)
plt.plot(t, complex_signal.real, label='Real Part', color='b', linestyle='--')
plt.plot(t, complex_signal.imag, label='Imaginary Part', color='r', linestyle='--')
plt.title('Complex Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid()
plt.legend()

plt.tight_layout()
plt.show()