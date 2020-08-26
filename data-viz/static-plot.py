import matplotlib.pyplot as plt
import numpy as np
import csv

# can change which file is being used with user input
# data_file = input("Please enter the name of the data file: ")
# if data_file.endswith(".csv") != True:
# 	data_file += ".csv"
data_file = "AAPG-Dataset-01.csv"

# load in the data to a numpy array
# similiar to pandas dataframe, just another option
data = np.genfromtxt(data_file, delimiter=',', skip_header=True)[:, 0:]

# set up how many subplots we want, and the size of the figure
fig, axs = plt.subplots(2, 2, figsize=(18, 12))
# assign each subplot with the data to be shown
axs[0, 0].scatter(data[:,0], data[:,4], c=data[:,29])
axs[0, 0].title.set_text("%Si vs. Depth Colored by Quartz")
axs[1, 0].scatter(data[:,4], data[:,29], c=data[:,29])
axs[1, 0].title.set_text("%Si vs. %Quartz Colored by Quartz")
axs[0, 1].scatter(data[:,0], data[:,8], c=data[:,32])
axs[0, 1].title.set_text("%Ca vs. Depth Colored by Calcite")
axs[1, 1].scatter(data[:,8], data[:,32], c=data[:,32])
axs[1, 1].title.set_text("%Ca vs. %Calcite Colored by Calcite")

plt.show()
# optionally save figure to a .png
#plt.savefig("Static-Plot.png")