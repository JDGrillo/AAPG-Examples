import matplotlib.pyplot as plt
import numpy as np

data_file = input("Please enter the name of the data file: ")
if data_file.endswith(".csv") != True:
	data_file += ".csv"

# data = np.loadtxt(open(data_file, "r"), dtype="float", delimiter=",", skiprows=1)
data = np.genfromtxt(data_file, delimiter=',', skip_header=True)[:, 1:]
# data = np.random.randn(2, 100)
print("data are", data)
print("data zero are", data[0])
print("first column zero are", data[:,0])
print("5th column zero are", data[:,4])

# fig, axs = plt.subplots(2, 2, figsize=(5, 5))
# axs[0, 0].hist(data[0])
# axs[1, 0].scatter(data[0], data[1])
# axs[0, 1].scatter(data[:,0], data[:,4])
plt.scatter(data[:,0], data[:,4])
# axs[1, 1].hist2d(data[0], data[1])

plt.savefig("temp.png")
# plt.show()