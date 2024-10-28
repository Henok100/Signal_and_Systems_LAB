# Import necessary libraries
import numpy as np  # For mathematical operations
import matplotlib.pyplot as plt  # For plotting

# Analog Signal (Square Wave) - Continuous Signal
t_analog = np.linspace(0, 1, 1000)  # Time from 0 to 1 second, 1000 samples
frequency = 5  # Frequency of 5 Hz for the square wave
analog_square_wave = np.sign(np.sin(2 * np.pi * frequency * t_analog))  # Generate analog square wave signal

# Digital Signal by Sampling the Analog Square Wave
sampling_rate = 40  # Set sampling rate for the digital signal
t_digital = np.arange(0, 1, 1/sampling_rate)  # Discrete time points for the digital signal
digital_square_wave = np.sign(np.sin(2 * np.pi * frequency * t_digital))  # Generate digital square wave by sampling

# Plot both analog and digital square waves in one figure with two rows
plt.figure(figsize=(10, 8))

# Plot the analog square wave signal in the first subplot (first row)
plt.subplot(2, 1, 1)  # 2 rows, 1 column, first subplot
plt.plot(t_analog, analog_square_wave, label="Analog Square Wave Signal")
plt.title("Analog Square Wave Signal")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.legend()

# Plot the digital square wave signal in the second subplot (second row)
plt.subplot(2, 1, 2)  # 2 rows, 1 column, second subplot
plt.stem(t_digital, digital_square_wave, basefmt=" ", label="Digital Square Wave Signal")
plt.title("Digital Square Wave Signal (Sampled)")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.legend()

# Display the combined plot
plt.tight_layout()  # Adjust layout to prevent overlapping
plt.show()