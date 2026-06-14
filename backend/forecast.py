from sklearn.ensemble import RandomForestRegressor
import numpy as np

X = np.array([
    [3000],
    [3500],
    [4000],
    [4500],
    [5000]
])

y = np.array([
    3200,
    3600,
    4300,
    4700,
    5400
])

model = RandomForestRegressor()

model.fit(X, y)

def predict_bill(data):
    prediction = model.predict([[data["current_bill"]]])

    return round(float(prediction[0]), 2)