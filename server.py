from fastapi import FastAPI, Body
from pydantic import BaseModel

from part3.part3 import predictCrop as predictCropSuitability


class CropData(BaseModel):
    n: int
    p: int
    k: int
    temp: int
    humidity: int
    ph: float
    rainfall: int

app = FastAPI()

@app.post("/predict/")
def predict_crop(data: CropData = Body(...)):

    n = data.n
    p = data.p
    k = data.k
    temp = data.temp
    humidity = data.humidity
    ph = data.ph
    rainfall = data.rainfall

    prediction = predictCropSuitability(n, p, k, temp, humidity, ph, rainfall)
    prediction_str = str(prediction)
    return {"predicted_crop": prediction_str}
