"""
Lab Example: Classification of Signals - Continuous-Time and Discrete-Time
In this example, we will represent and visualize continuous-time and discrete-time signals
using Python. We will plot both signal types and highlight their differences.
"""

# Import necessary libraries
import numpy as np  # For numerical operations
import matplotlib.pyplot as plt  # For plotting graphs

# Continuous-Time Signal
# A continuous signal is defined over a continuous range of time (e.g., sin(t))
# Let's define a continuous-time signal as a sine wave

# Time variable for continuous signal (defined over a range with small intervals)
t_continuous = np.linspace(0, 2 * np.pi, 100)  # Time from 0 to 2π with 100 samples
# Explanation: np.linspace(start, stop, num) creates an array of 'num' evenly spaced samples 
# from 'start' to 'stop'.

continuous_signal = np.sin(t_continuous)  # Define sine wave as continuous signal
# Explanation: np.sin(x) computes the sine of x (in radians), where x can be an array.

# Discrete-Time Signal
# A discrete signal is only defined at specific time intervals (e.g., sin(n) at integer values of n)
# Let's define a discrete-time signal using sampled points of the sine wave

# Time variable for discrete signal (discrete points in time)
t_discrete = np.arange(0, 2 * np.pi, np.pi / 4)  # Time from 0 to 2π with a step size of π/4
# Explanation: np.arange(start, stop, step) creates an array of values from 'start' to 'stop' 
# with increments of 'step'.

discrete_signal = np.sin(t_discrete)  # Define sine wave as discrete signal

# Plotting the signals
plt.figure(figsize=(12, 6))  # Set the figure size

# Plot continuous signal
plt.subplot(2, 1, 1)  # Create a subplot for the first graph (2 rows, 1 column, 1st position)
plt.plot(t_continuous, continuous_signal, label='Continuous Signal (Sine Wave)')
plt.title("Continuous-Time Signal")  # Title of the plot
plt.xlabel("Time")  # Label for x-axis
plt.ylabel("Amplitude")  # Label for y-axis
plt.grid(True)  # Show grid
plt.legend()  # Show legend to identify the signal

# Plot discrete signal
plt.subplot(2, 1, 2)  # Create a subplot for the second graph (2 rows, 1 column, 2nd position)
plt.stem(t_discrete, discrete_signal, label='Discrete Signal (Sampled Sine Wave)')
# Explanation: plt.stem(x, y) creates a stem plot with stems at each (x, y) coordinate. 


plt.title("Discrete-Time Signal")  # Title of the plot
plt.xlabel("Time")  # Label for x-axis
plt.ylabel("Amplitude")  # Label for y-axis
plt.grid(True)  # Show grid
plt.legend()  # Show legend

# Display the plots
plt.tight_layout()  # Adjust layout to fit all elements
plt.show()  # Show the plot window
