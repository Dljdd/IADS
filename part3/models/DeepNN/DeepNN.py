import models.DeepNN.cropRecDataFrame as crdf
import tensorflow as tf
import pandas as pd
import numpy as np
from tensorflow.python.keras.layers import Dense

class cropRecModel:
  def __init__(self) -> None:
    self.crops_list = ['rice', 'maize', 'jute', 'cotton', 'coconut', 'papaya', 'orange', 'apple', 'muskmelon',
              'watermelon', 'grapes', 'mango', 'banana', 'pomegranate', 'lentil', 'blackgram',
              'mungbean', 'mothbeans', 'pigeonpeas', 'kidneybeans', 'chickpea', 'coffee']
    self.model = self.gen_model()

    data = np.array([[40,60,20,25,50,31.5,60]])
    self.model.predict(data)
    
    self.model.load_weights(r"C:\Users\ozada\OneDrive\Documents\sem 4\python\Github\IADS\part3\models\DeepNN\Crop_Recommender_weights.h5")

  def gen_model(self):
    model = tf.keras.models.Sequential([
        Dense(35, activation = 'relu', input_shape = crdf.X.shape[1:]),
        Dense(49, activation = 'relu'),
        Dense(35, activation = 'relu'),
        Dense(22, activation = 'softmax')
    ])
    model.compile(optimizer='adam', loss = 'categorical_crossentropy',metrics = ['accuracy'])
    return model

  def getPrediction(self, custom_data):
    custom_data = crdf.scaler.transform(custom_data)
    custom_data = pd.DataFrame(custom_data, columns = crdf.xcols)

    custom_prediction = self.model.predict(custom_data)

    return self.crops_list[np.argmax(custom_prediction)]
  
  def getPredictionTopN(self, custom_data, n=3):
    custom_data = crdf.scaler.transform(custom_data)
    custom_data = pd.DataFrame(custom_data, columns = crdf.xcols)

    custom_prediction = self.model.predict(custom_data)

    top_n_indices = np.argsort(custom_prediction[0])[::-1][:n]

    top_n_crops = [self.crops_list[i] for i in top_n_indices]

    return top_n_crops


