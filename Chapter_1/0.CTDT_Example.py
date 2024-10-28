# Import necessary libraries
import numpy as np  # For mathematical operations
import matplotlib.pyplot as plt  # For plotting

# Define the analog signal (continuous sinusoidal wave)
t_analog = np.linspace(0, 1, 1000)  # Time from 0 to 1 second, with 1000 samples for smoothness
frequency = 5  # Set the frequency to 5 Hz
analog_signal = np.sin(2 * np.pi * frequency * t_analog)  # Generate the analog sinusoidal signal

# Define the digital signal by sampling the analog signal
sampling_rate = 20  # Set sampling rate for the digital signal
t_digital = np.arange(0, 1, 1/sampling_rate)  # Create discrete time points for digital signal
digital_signal = np.round(np.sin(2 * np.pi * frequency * t_digital))  # Quantize analog values for digital signal

# Plot both signals in a single figure with two rows
plt.figure(figsize=(10, 8))

# Plot the analog signal in the first subplot (first row)
plt.subplot(2, 1, 1)  # 2 rows, 1 column, first subplot
plt.plot(t_analog, analog_signal, label="Analog Signal")
plt.title("Analog Signal: Continuous Sinusoidal Wave")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.legend()

# Plot the digital signal in the second subplot (second row)
plt.subplot(2, 1, 2)  # 2 rows, 1 column, second subplot
plt.stem(t_digital, digital_signal, basefmt=" ", label="Digital Signal")
plt.title("Digital Signal: Quantized Sinusoidal Wave")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.legend()

# Display the combined plot
plt.tight_layout()  # Adjust layout to prevent overlapping
plt.show()
