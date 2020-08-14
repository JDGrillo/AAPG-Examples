import lasio
import numpy as np
from datetime import datetime
import os

key = input("Please enter the name of the legend: ")
data = input("Please enter the name of the sheet to be LAS'd: ")
file_name = input("Please enter the name of the save file: ")
if key.endswith(".csv") != True:
	key += ".csv"
if data.endswith(".csv") != True:
	data += ".csv"

keys = np.loadtxt(open(key, "r"), dtype="str", delimiter=",", skiprows=1)
	
datas = np.loadtxt(open(data, "r"), delimiter=",", skiprows=1)

xrf_las = lasio.LASFile()
xrf_las.version.WRAP
xrf_las.well.DATE = str(datetime.today())
xrf_las.well.API = str("")
xrf_las.well.COMP = ""
xrf_las.well.WELL = ""

for i in range(len(keys)):
	xrf_las.add_curve(keys[i][0], datas[:,i], unit=keys[i][1], descr=keys[i][2])
	
xrf_las.write(str(file_name + ".las"), STEP=1, version =1.2)