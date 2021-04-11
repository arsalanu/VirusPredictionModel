import numpy as np 
import pandas as pd
import tensorflow.compat.v1 as tf
from tensorflow import keras

sess = tf.Session(config=tf.ConfigProto(log_device_placement=True))

class CovModel(keras.Model):
    def __init__(self, hidden_units):
        super(CovModel, self).__init__()
        self.hidden_units = hidden_units
        self.dense_layers = [keras.layers.Dense(u) for u in hidden_units]

    def call(self, inputs):
        x = inputs
        for layer in self.dense_layers:
            x = layer(x)
        return x

    def get_config(self):
        return {"hidden_units": self.hidden_units}

    @classmethod
    def from_config(cls, config):
        return cls(**config)



model_c = keras.models.load_model(
    "cov_pred_model", custom_objects={"CustomModel": CovModel}
)

ndataset = np.genfromtxt('PatientData.csv', dtype=int, delimiter=',')

sampledata = ndataset[3000:,1:7]
sampleresults = ndataset[3000:,7:]

predictions = (model_c.predict(sampledata) > 0.5).astype("int32") 

count = [0,0]
for i in range(len(sampleresults)):
    count[0] += 1
    pred_out = [predictions[i][0],predictions[i][1],predictions[i][2]]
    actual_out = [sampleresults[i][0],sampleresults[i][1],sampleresults[i][2]]
    if pred_out == actual_out:
        count[1] += 1

print("Score: ", count[1], "/", count[0], "|| Total accuracy: ",(count[1]/count[0])*100,"%")


