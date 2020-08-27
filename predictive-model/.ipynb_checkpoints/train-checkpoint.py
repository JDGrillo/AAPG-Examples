import keras
import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import SGD

# data_file = input("Please enter the name of the data file: ")
# if data_file.endswith(".csv") != True:
# 	data_file += ".csv"
data_file = "data-files/AAPG-Training-Dataset.csv"

data = np.loadtxt(data_file, delimiter=",", skiprows=1)

input_data = data[:,0:9]
output_data = data[:,9:]

model = Sequential()
model.add(Dense(9, input_dim=9, activation='relu'))
model.add(Dense(9, activation='relu'))
model.add(Dense(9))

optimizer = keras.optimizers.RMSprop(0.001)

model.compile(loss='mean_squared_error', optimizer=optimizer, metrics=['mse'])

model.fit(input_data, output_data, epochs=250, batch_size=10)

predicted_data = model.predict(input_data)

_, accuracy = model.evaluate(input_data, output_data)

print("The mean squared error accuracy is", accuracy)

model.save("models/aapg-model.h5")