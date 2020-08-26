import matplotlib.pyplot as plt
import numpy as np
import csv

# data_file = input("Please enter the name of the data file: ")
# if data_file.endswith(".csv") != True:
# 	data_file += ".csv"
data_file = "AAPG-Dataset-01.csv"

data = np.genfromtxt(data_file, delimiter=',', skip_header=True)[:, 0:]

with open(data_file, mode="r", encoding="utf-8-sig") as f:
    d_reader = csv.DictReader(f)
    data_headers = d_reader.fieldnames

fig, axs = plt.subplots(2, 2, figsize=(15, 10))
axs[0, 0].scatter(data[:,0], data[:,4], c=data[:,29])
axs[0, 0].title.set_text("%Si vs. Depth Colored by Quartz")
axs[1, 0].scatter(data[:,4], data[:,29], c=data[:,29])
axs[1, 0].title.set_text("%Si vs. %Quartz Colored by Quartz")
axs[0, 1].scatter(data[:,0], data[:,8], c=data[:,32])
axs[0, 1].title.set_text("%Ca vs. Depth Colored by Calcite")
axs[1, 1].scatter(data[:,8], data[:,32], c=data[:,32])
axs[1, 1].title.set_text("%Ca vs. %Calcite Colored by Calcite")

plt.savefig("Static-Plot.png")