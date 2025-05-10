# list - list include import
import numpy as np

# like beautifulsoup
import statsmodels.api as sm

size = np.array([170,180,160,165,158,176,182,172]).reshape((-1,1))
weight = [75,81,59,70,55,78,84,72]

model = sm.OLS(weight, size).fit()
print(model.summary())

# 실행 결과물
# info R-squared (uncentered)은 R값으로 0~1
#  Prob (F-statistic)은 ex) y=ax+b 중에서 a가 0일 것이다라고 가정하고 진행하는데 a가 0일 확률이, 1.03e-08임 (0.0000000103)
#  즉, a가 0일 확률이 매우 낮으니 a는 0이 아니며 서로 관계가 있다는 것을 증명한 것임. (a가 0이면 x에 어떠한 값을 넣어도 변화가 없기 때문)
#  AIC의 값이 적을수록 다른 모델에 비해서 좋음
# note coef는 a값 (y=ax+b)
# std err는 표준편차
# P>|t|는 0.5 이하로 값을 띄면 유의미한 coefficent
# 100번 작업을 진행하면 coef 값이 95%[0.025-0.975] 확률로 0.390 - 0.455 사이 안에 들어갈 것이다

#                                  OLS Regression Results                                
# =======================================================================================
# Dep. Variable:                      y   R-squared (uncentered):                   0.993
# Model:                            OLS   Adj. R-squared (uncentered):              0.992
# Method:                 Least Squares   F-statistic:                              936.5
# Date:                Sat, 10 May 2025   Prob (F-statistic):                    1.03e-08
# Time:                        14:16:39   Log-Likelihood:                         -25.993
# No. Observations:                   8   AIC:                                      53.99
# Df Residuals:                       7   BIC:                                      54.06
# Df Model:                           1                                                  
# Covariance Type:            nonrobust                                                  
# ==============================================================================
#                  coef    std err          t      P>|t|      [0.025      0.975]
# ------------------------------------------------------------------------------
# x1             0.4228      0.014     30.603      0.000       0.390       0.455
# ==============================================================================
# Omnibus:                        1.641   Durbin-Watson:                   2.315
# Prob(Omnibus):                  0.440   Jarque-Bera (JB):                0.998
# Skew:                          -0.767   Prob(JB):                        0.607
# Kurtosis:                       2.199   Cond. No.                         1.00
# ==============================================================================