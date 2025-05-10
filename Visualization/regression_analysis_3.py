import numpy as np
import statsmodels.api as sm
import pandas as pd

data = pd.read_csv('california_housing.csv')

# print(data)

# year, rooms, bedrooms : x, price : y
model = sm.OLS(data['price'], data[['year', 'rooms', 'bedrooms']]).fit()
print(model.summary())

pr = model.predict([20, 1000, 300])
print(pr)