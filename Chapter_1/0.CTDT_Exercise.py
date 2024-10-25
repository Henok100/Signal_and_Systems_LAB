"""
Exercise Solution: Classification of Signals - Continuous-Time and Discrete-Time
In this solution, we will represent and visualize continuous-time and discrete-time cosine signals.
"""

# Import necessary libraries
import numpy as np  # For numerical operations
import matplotlib.pyplot as plt  # For plotting graphs

# Continuous-Time Signal (Cosine Wave)
t_continuous_cos = np.linspace(0, 4 * np.pi, 200)  # Time from 0 to 4π with 200 samples
continuous_signal_cos = np.cos(t_continuous_cos)  # Define cosine wave as continuous signal

# Discrete-Time Signal (Cosine Wave)
t_discrete_cos = np.arange(0, 4 * np.pi, np.pi / 3)  # Time from 0 to 4π with a step size of π/3
discrete_signal_cos = np.cos(t_discrete_cos)  # Define cosine wave as discrete signal

# Plotting the cosine signals
plt.figure(figsize=(12, 6))  # Set the figure size

# Plot continuous cosine signal
plt.subplot(2, 1, 1)  # Create a subplot for the first graph (2 rows, 1 column, 1st position)
plt.plot(t_continuous_cos, continuous_signal_cos, label='Continuous Signal (Cosine Wave)')
plt.title("Continuous-Time Cosine Signal")  # Title of the plot
plt.xlabel("Time")  # Label for x-axis
plt.ylabel("Amplitude")  # Label for y-axis
plt.grid(True)  # Show grid
plt.legend()  # Show legend to identify the signal

# Plot discrete cosine signal
plt.subplot(2, 1, 2)  # Create a subplot for the second graph (2 rows, 1 column, 2nd position)
plt.stem(t_discrete_cos, discrete_signal_cos, label='Discrete Signal (Sampled Cosine Wave)')
plt.title("Discrete-Time Cosine Signal")  # Title of the plot
plt.xlabel("Time")  # Label for x-axis
plt.ylabel("Amplitude")  # Label for y-axis
plt.grid(True)  # Show grid
plt.legend()  # Show legend

# Display the plots
plt.tight_layout()  # Adjust layout to fit all elements
plt.show()  # Show the plot window
