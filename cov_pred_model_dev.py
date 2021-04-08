import numpy as np 
import pandas as pd
from tensorflow import keras
from keras.constraints import maxnorm
ndataset = np.genfromtxt('PatientData.csv', dtype=int, delimiter=',')

#training data
main_train_inp = ndataset[1:2000,1:7]
bin_train_inp = ndataset[1:2000,7:]

#test data
main_test_out = ndataset[2000:3000,1:7]
bin_test_out = ndataset[2000:3000,7:]

#model development
model = keras.models.Sequential()

model.add(keras.layers.Dense(12, input_dim=6, activation='relu'))
model.add(keras.layers.Dense(18, activation='relu'))
model.add(keras.layers.Dense(12, activation='relu'))
model.add(keras.layers.Dense(3, activation='softmax')) #output

model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(main_train_inp, bin_train_inp, epochs=300, batch_size=12)

model.save('cov_pred_model')

__,accuracy = model.evaluate(main_test_out, bin_test_out)
print('Test Data Accuracy: {}%'.format(accuracy*100))