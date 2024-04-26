# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 04:48:44 2021

@author: lenovo
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 19:21:21 2020

@author: abz1e14
"""
from pandas import read_excel
import pandas as pd
from statsmodels.tsa.api import ExponentialSmoothing
from matplotlib import pyplot

series = read_excel('K54Ddata_32049072.xlsx', sheet_name='Data', header=0, index_col=0, parse_dates=True, squeeze=True)
#series = series[-72:]

# ===================================
# Holt-Winter method in different scenarios # 
# ===================================
# ===================================
# Model 1: Holt-Winter method with additive trend and multiplicative seasonality 
# Here, alpha, beta, gamma are optimized
# ===================================
fit1 = ExponentialSmoothing(series, seasonal_periods=12, trend='add', seasonal='mul').fit()

# ===================================
# Model 2: Holt-Winter method with additive trend and multiplicative seasonality and Damped values and BoxCox Fit
# Here, the parameters alpha, beta, and gamma are optimized
# ===================================
fit2 = ExponentialSmoothing(series, seasonal_periods=12, trend='add', seasonal='mul', damped=True).fit(use_boxcox = True)

# ===================================
# Model 3: Holt-Winter method with additive trend and multiplicative seasonality
# Here, the parameters alpha = 0.2, beta = 0.0, and gamma = 0.6
# ===================================
fit3 = ExponentialSmoothing(series, seasonal_periods=12, trend='add', seasonal='mul', damped=True).fit(smoothing_level = 0.2, smoothing_slope=0.0,  smoothing_seasonal=0.6)

print("\n********************************\nForecasting Monthly Average of Weekly Pay (K54D) with Holt-Winters method\n")

#=====================================
# Time and forecast plots
#=====================================

series.plot(label = 'Time plot of original K54D series', legend=True)
fit1.forecast(12).plot(label = 'Model 1: Opt HW-Multiplicative seasonality',color='red', legend=True)
fit1.fittedvalues.plot(color='red',legend=False)

pyplot.xlabel('Year')
pyplot.ylabel('Avg pay')
pyplot.title('Holt-Winter\'s'' forecasts for K54D Data')
pyplot.show()

series.plot(label = 'Time plot of original K54D series', legend=True)
fit2.forecast(12).plot(label = 'Model 2: Opt HW-Multiplicative seasonality_Damped',color='green', legend=True)
fit2.fittedvalues.plot(color='green')

pyplot.xlabel('Year')
pyplot.ylabel('Avg pay')
pyplot.title('Holt-Winter\'s'' forecasts for K54D Data')
pyplot.show()

series.plot(label = 'Time plot of original K54D series', legend=True)
fit3.forecast(12).plot(label = 'Model 3:\nHW-Multiplicative seasonality_\nAlpha=0.2,\nBeta=0.0,Gamma=0.6',color='green', legend=True)
fit3.fittedvalues.plot(color='green')

pyplot.xlabel('Year')
pyplot.ylabel('Avg pay')
pyplot.title('Holt-Winter\'s'' forecasts for K54D Data')
pyplot.show()


#====================================
# Evaluating the errors 
#====================================
from sklearn.metrics import mean_squared_error 
MSE1=mean_squared_error(fit1.fittedvalues, series)
MSE2=mean_squared_error(fit2.fittedvalues, series)
MSE3=mean_squared_error(fit3.fittedvalues, series)

#=====================================
# Printing the paramters and errors for each scenario
#=====================================
results=pd.DataFrame(index=[r"alpha", r"beta", r"gamma", r"l0", "b0", "MSE"])
params = ['smoothing_level', 'smoothing_slope', 'smoothing_seasonal', 'initial_level', 'initial_slope']
results["HW model 1"] = [fit1.params[p] for p in params] + [MSE1]
results["HW model 2"] = [fit2.params[p] for p in params] + [MSE2]
results["HW model 3"] = [fit3.params[p] for p in params] + [MSE3]
print(results)

#=====================================
# Evaluating and plotting the residual series for each scenario
#=====================================
residuals1= fit1.fittedvalues - series
residuals2= fit2.fittedvalues - series
residuals3= fit3.fittedvalues - series

residuals1.rename('residual plot for model 1').plot(color='red', legend=True)
residuals2.rename('residual plot for model 2').plot(color='blue', legend=True)
residuals3.rename('residual plot for model 3').plot(color='blue', legend=True)

pyplot.title('Residual plots for models 1-3')
pyplot.show()

#=====================================
# ACF plots of the residual series for each scenario
#=====================================
from statsmodels.graphics.tsaplots import plot_acf
plot_acf(residuals1, title='Residual ACF for model 1', lags=50)
plot_acf(residuals2, title='Residual ACF for model 2', lags=50)
plot_acf(residuals3, title='Residual ACF for model 3', lags=50)
pyplot.show()
