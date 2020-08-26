import lasio
import numpy as np
from datetime import datetime
import os

# get user input as to which files they would like to use
key = input("Please enter the name of the legend: ")
data = input("Please enter the name of the sheet to be LAS'd: ")
file_name = input("Please enter the name of the save file: ")
# check to make sure they are .csv files
if key.endswith(".csv") != True:
    key += ".csv"
if data.endswith(".csv") != True:
    data += ".csv"

# load the data from the key csv
keys = np.loadtxt(open(key, "r"), dtype="str", delimiter=",", skiprows=1)

# load the data from the datasheet
dataset = np.genfromtxt(data, delimiter=',', skip_header=True)[:, 0:]

# assign necessary attributes to xrf_las object
xrf_las = lasio.LASFile()
xrf_las.version.WRAP
xrf_las.well.DATE = str(datetime.today())
xrf_las.well.API = str("")
xrf_las.well.COMP = ""
xrf_las.well.WELL = ""

# iterate over all keys, and add curve of corresponding data column
for i in range(len(keys)):
#   on the first pass, we're adding ("Depth (ft)", The Column of Depth Data, "ft", "Value") to our xrf_las object
#   on the second pass, we're adding ("%Na", The Column of Na Data, "wt_pct", "XRF Sodium") to our xrf_las object
    xrf_las.add_curve(keys[i][0], dataset[:,i], unit=keys[i][1], descr=keys[i][2])

# write the xrf_las object into an .las file specified by user
xrf_las.write(str(file_name + ".las"), STEP=1, version =1.2)