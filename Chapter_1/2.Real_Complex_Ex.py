import numpy as np
import matplotlib.pyplot as plt

# Set parameters for the signals
frequencies = [1, 2, 5]  # Frequencies for the complex signal (Hz)
sampling_rate = 100  # Sampling rate in Hz
duration = 2  # Duration in seconds
t = np.linspace(0, duration, sampling_rate * duration, endpoint=False)  # Time vector

# --- Exercise 1: Generate and Analyze a Real Signal ---
# Generate a cosine wave
real_signal = np.cos(2 * np.pi * frequencies[0] * t)  # Cosine wave with frequency 1 Hz

# Plotting the cosine wave
plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
plt.plot(t, real_signal, label='Real Signal (Cosine Wave)', color='b')
plt.title('Real Signal: Cosine Wave')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid()
plt.legend()

# --- Exercise 2: Manipulate Complex Signals ---
# Initialize a plot for complex signals
plt.subplot(2, 1, 2)

# Loop through different frequencies to plot complex signals
for freq in frequencies:
    # Generate complex signal for the current frequency
    complex_signal = np.exp(1j * 2 * np.pi * freq * t)
    
    # Plot real and imaginary parts of the complex signal
    plt.plot(t, complex_signal.real, label=f'Real Part at {freq} Hz', linestyle='--')
    plt.plot(t, complex_signal.imag, label=f'Imaginary Part at {freq} Hz', linestyle=':')

plt.title('Complex Signals: Real and Imaginary Parts')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid()
plt.legend()

plt.tight_layout()
plt.show()