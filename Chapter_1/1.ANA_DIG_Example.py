# Import necessary libraries
import numpy as np  # For mathematical operations
import matplotlib.pyplot as plt  # For plotting

# Analog Signal: Sinusoidal Wave
# Define time range for analog signal
t_analog = np.linspace(0, 1, 1000)  # 0 to 1 second, 1000 samples
frequency = 5  # Frequency of 5 Hz for the analog signal
analog_signal = np.sin(2 * np.pi * frequency * t_analog)

# Plot analog signal
plt.figure(figsize=(10, 4))
plt.plot(t_analog, analog_signal, label="Analog Signal")
plt.title("Analog Signal: Continuous Sinusoidal Wave")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.legend()
plt.show()

# Digital Signal: Digitize the analog signal with a threshold
sampling_rate = 20  # Sampling frequency of 20 Hz for digitization
t_digital = np.arange(0, 1, 1/sampling_rate)  # Discrete time points
digital_signal = np.round(np.sin(2 * np.pi * frequency * t_digital))

# Plot digital signal
plt.figure(figsize=(10, 4))
plt.stem(t_digital, digital_signal, basefmt=" ", label="Digital Signal")
plt.title("Digital Signal: Quantized Sinusoidal Wave")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.legend()
plt.show()