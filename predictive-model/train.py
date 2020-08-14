import keras
from numpy import loadtxt
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import SGD

data_file = input("Please enter the name of the data file: ")
if data_file.endswith(".csv") != True:
	data_file += ".csv"

data = loadtxt(data_file, delimiter=",", skiprows=1)

input_data = data[:,0:9]
output_data = data[:,9]

model = Sequential()
model.add(Dense(9, input_dim=9, activation='relu'))
# model.add(Dense(9, activation='relu'))
model.add(Dense(1, kernel_initializer='normal'))

model.compile(loss='mean_squared_error', optimizer="adam", metrics=['accuracy'])

model.fit(input_data, output_data, epochs=10000, batch_size=10)

_, accuracy = model.evaluate(input_data, output_data)
print('Accuracy: %.2f' % (accuracy*100))