import pandas as pd
from sklearn.preprocessing import StandardScaler

df = pd.read_csv(r"part3/models/DeepNN/cropRecData.csv")

X = df.drop(columns = ['label'])
     
scaler = StandardScaler()
xcols = X.columns
X = scaler.fit_transform(X)
X = pd.DataFrame(X, columns = xcols)