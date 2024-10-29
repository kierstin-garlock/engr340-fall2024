
import matplotlib.pyplot as plt
import numpy as np

# import the CSV file using numpy
path = '../../../data/ekg/mitdb_201.csv'

# load data in matrix from CSV file; skip first two rows

### Your code here ###
data = np.loadtxt(path, delimiter=",", skiprows=2)

# save each vector as own variable

### Your code here ###
V1 = data[:,0]
V2 = data[:,1]
V3 = data[:,2]

# use matplot lib to generate a single

### Your code here ##
plt.title("ekg data signal")
plt.xlabel("Time (s)")
plt.ylabel("mV")
plt.plot(V1, V2)
plt.plot(V1, V3)
plt.show()