import matplotlib.pyplot as plt
import numpy as np
import csv

# can change which file is being used with user input
# data_file = input("Please enter the name of the data file: ")
# if data_file.endswith(".csv") != True:
# 	data_file += ".csv"
data_file = "AAPG-Dataset-01.csv"

# set up dictionary to know where element references are
# for example, if the user is wanting to plot Si, we know to look at the 5th column in our csv
data_dictionary = {
    "depth": 0,
    "na": 1,
    "mg": 2,
    "al": 3,
    "si": 4,
    "p": 5,
    "s": 6,
    "k": 7,
    "ca": 8,
    "ti": 9,
    "mn": 10,
    "fe": 11,
    "v": 12,
    "cr": 13,
    "co": 14,
    "ni": 15,
    "cu": 16,
    "zn": 17,
    "ga": 18,
    "as": 19,
    "pb": 20,
    "th": 21,
    "rb": 22,
    "u": 23,
    "sr": 24,
    "y": 25,
    "zr": 26,
    "nb": 27,
    "mo": 28,
    "quartz": 29,
    "dolomite": 30,
    "illite": 31,
    "calcite": 32,
    "gypsum": 33,
    "microcline": 34,
    "albite": 35,
    "pyrite": 36,
    "kaolinite": 37,
}

# load in the data to a numpy array
data = np.genfromtxt(data_file, delimiter=',', skip_header=True)[:, 0:]

# get user input as to what they want to see plotted
# notice the .lower() function call to match what is in our dictionary
x = input("Please the first attribute to be plotted: ").lower()
y = input("Please the second attribute to be plotted: ").lower()
color = input("Please the attribute to be colored by: ").lower()

# set the size of the figure to be created
plt.figure(figsize=(18, 12))
# create a scatter plot using the response from the user, and which dicionary value those response relate to
# for example, if the user asks for Calcite, data[:,data_dictionary[x]] becomes data[:,32]
# the [:,] syntax is used to select a 'slice' of data, which in this context is a column from csv
plt.scatter(data[:,data_dictionary[x]], data[:,data_dictionary[y]], c=data[:,data_dictionary[color]])
plt.title(f"""{x} vs {y} colored by {color}""")
plt.show()
# optionally save figure to a .png
# plt.savefig("Dyanmic-Plot.png")