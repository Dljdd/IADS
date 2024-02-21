from fastapi import FastAPI, Body
from pydantic import BaseModel

#from part3.part3 import predictCrop as predictCropSuitability
from part3.croprecommendation import predictCrop
from part1.modelprediction import makePrediction
class CropData(BaseModel):
    n: float
    p: float
    k: float
    temp: float
    humidity: float
    ph: float
    rainfall: float

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/predict")
async def predict_crop(data: CropData = Body(...)):
    """
    Example Json:
        {
      "n": 21,
      "p": 32,
      "k": 31,
      "temp": 22,
      "humidity": 47,
      "ph": 7.2,
      "rainfall": 22
    }
    Output:
    {
    "predicted_crop": "mothbeans"
    }
    """

    n = data.n
    p = data.p
    k = data.k
    temp = data.temp
    humidity = data.humidity
    ph = data.ph
    rainfall = data.rainfall

    prediction = predictCrop(n, p, k, temp, humidity, ph, rainfall)
    prediction_str = str(prediction)
    return {"predicted_crop": prediction_str}

@app.post("/identify_disease")
async def identify_disease(img_path):
    """
    Example Json file
    """
    pred = makePrediction(img_path)
    return {"predicted_disease": f"{pred}"}