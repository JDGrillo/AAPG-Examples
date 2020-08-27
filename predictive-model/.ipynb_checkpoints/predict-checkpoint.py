import keras
import numpy as np
import pandas as pd
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import SGD

# data_file = input("Please enter the name of the data file: ")
# if data_file.endswith(".csv") != True:
# 	data_file += ".csv"
data_file = "data-files/AAPG-Prediction-Dataset.csv"

data = np.loadtxt(data_file, delimiter=",", skiprows=1)

input_data = data[:,0:9]

model = keras.models.load_model("models/aapg-model.h5")

predicted_data = model.predict(input_data)
headers = ["Modeled Quartz", "Modeled Dolomite", "Modeled Illite", "Modeled Calcite", "Modeled Gypsum", "Modeled Microclin", "Modeled Albite", "Modeled Pyrite", "Modeled Kaolinite"]

predicted_df = pd.DataFrame(data = predicted_data, columns = headers)

master_df = pd.read_csv("data-files/AAPG-Master-Dataset.csv")

master_df = master_df.join(predicted_df, how="outer")
master_df.to_csv("data-files/Joined-Master-Dataset.csv", index=False)
