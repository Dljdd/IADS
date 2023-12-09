
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import classification_report
from sklearn import metrics
from sklearn.model_selection import cross_val_score
import pickle






def predictCrop(n :int, p :int, k :int, temperature :int, humidity: int, ph:float, rainfall: int):
    """
    json template
    {
  "n": 10,
  "p": 40,
  "k": 20,
  "temp": 20,
  "humidity": 10,
  "ph": 6.5,
  "rainfall": 1
}

    """
    with open('/Users/dylanmoraes/Desktop/Py_Lecture/Intelligent_CropPrediction_System-main/models/RandomForest.pkl', 'rb') as f:
        RF = pickle.load(f)
    # Create input data array 
    data = np.array([[n, p, k, temperature, humidity, ph, rainfall]])
    prediction = RF.predict(data)
    print(prediction)
    # prediction logic 
    # returns predicted crop name
    return prediction


