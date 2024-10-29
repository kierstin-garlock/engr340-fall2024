import matplotlib.pyplot as plt
import numpy as np

"""
Step 0: Select which database you wish to use.
"""

# database name
database_name = 'mitdb_201'

# path to ekg folder
path_to_folder = "../../../data/ekg/"

# select a signal file to run
signal_filepath = path_to_folder + database_name + ".csv"

"""
Step #1: load data in matrix from CSV file; skip first two rows. Call the data signal.
"""

#signal = 0
## YOUR CODE HERE ##
signal = np.loadtxt(signal_filepath, delimiter=",", skiprows=2)

V1 = signal[:,0]    # Elapsed Time
V2 = signal[:,1]    # MLII
V3 = signal[:,2]    #mV

"""
Step 2: (OPTIONAL) pass data through LOW PASS FILTER (fs=250Hz, fc=15, N=6). These may not be correctly in radians
"""

## YOUR CODE HERE ##

"""
Step 3: Pass data through weighted differentiator 
"""

## YOUR CODE HERE ##
differentiator = np.diff(V3)


"""
Step 4: Square the results of the previous step
"""
 ## YOUR CODE HERE ##
squared_signal = differentiator ** 2

"""
Step 5: Pass a moving filter over your data
"""

## YOUR CODE HERE
ones = np.ones(10)
smooth_signal = np.convolve(squared_signal, ones, 'same')
# make a plot of the results. Can change the plot() parameter below to show different intermediate signals
#plt.title('Process Signal for ' + database_name)
#plt.plot(signal)
#plt.show()

# Raw Signal Plot
plt.title("ekg raw data signal")
plt.xlabel("Time (s)")
plt.ylabel("mV")
plt.plot(V1, V3)
plt.show()

# Differentiator Plot
plt.title("ekg weighted differentiator signal")
plt.xlabel("Time (s)")
plt.ylabel("Differentiated Voltage")
plt.plot(V1[1:], differentiator)
plt.show()


# Squared Plot
plt.title("ekg squared data signal")
plt.xlabel("Time (s)")
plt.ylabel("Squared Voltage")
plt.plot(V1[1:], squared_signal)
plt.show()


# Moving Filter Plot
plt.title("ekg moving filter signal")
plt.xlabel("Time (s)")
plt.ylabel("Smoothed Filter Voltage")
plt.plot(V1[1:], smooth_signal)
plt.show()