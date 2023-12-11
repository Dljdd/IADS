import numpy as np
from cropRates import cropRates
from models.DeepNN.DeepNN import cropRecModel

NNmodel = cropRecModel()

def predictCropProfit(custom_data):
    custom_prediction = NNmodel.getPredictionTopN(custom_data, n=3)
    # print(custom_prediction)

    prices = []
    for crop in custom_prediction:
        prices.append(cropRates[crop])

    Area = float(input("Please enter your Area in Hectares: "))

    for idx, price in enumerate(prices):
        prices[idx] = float(price) * Area

    profit1 = prices[1] - prices[0]
    profit2 = prices[2] - prices[0]

    threshold1 = 40000
    threshold2 = 80000

    if profit1 >= threshold1:
        if profit2 >= threshold2:
            if profit2 > profit1:
                return custom_prediction[2]
            else:
                return custom_prediction[1]
        else:
            return custom_prediction[1]
    elif profit2 >= threshold2:
        return custom_prediction[2]
    else:
        return custom_prediction[0]
    
custom_data = np.array([[77, 49, 42, 20, 82, 6.5, 202]])
custom_prediction = predictCropProfit(custom_data)
print(f"Suitable Crop w.r.t. profit is {custom_prediction}")