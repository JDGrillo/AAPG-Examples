import matplotlib.pyplot as plt
import numpy as np
import csv

# data_file = input("Please enter the name of the data file: ")
# if data_file.endswith(".csv") != True:
# 	data_file += ".csv"
data_file = "AAPG-Dataset-01.csv"

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

data = np.genfromtxt(data_file, delimiter=',', skip_header=True)[:, 0:]

x = input("Please the first attribute to be plotted: ").lower()
y = input("Please the second attribute to be plotted: ").lower()
color = input("Please the attribute to be colored by: ").lower()

plt.scatter(data[:,data_dictionary[x]], data[:,data_dictionary[y]], c=data[:,data_dictionary[color]])
plt.title(f"""{x} vs {y} colored by {color}""")

plt.savefig("Dyanmic-Plot.png")