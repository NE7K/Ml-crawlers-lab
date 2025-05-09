# list - list include import
import numpy as np

# like beautifulsoup
import statsmodels.api as sm

size = np.array([170,180,160,165,158,176,182,172]).reshape((-1,1))
weight = [75,81,59,70,55,78,84,72]

model = sm.OLS(weight, size).fit()
print(model.summary())

