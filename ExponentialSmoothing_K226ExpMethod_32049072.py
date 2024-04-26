# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 19:05:53 2020

@author: abz1e14
"""
from pandas import read_excel
import pandas as pd
from statsmodels.tsa.api import Holt
from matplotlib import pyplot
series = read_excel('K226data_32049072.xlsx', sheet_name='Data', header=0, index_col=0, parse_dates=True, squeeze=True)

# ===================================
# Simple Exponential Smoothing #
# ===================================
# Holt model 1: alpha = 0.5, beta=0.5
fit1 = Holt(series).fit(smoothing_level=0.55, smoothing_slope=0.01, optimized=False)
fcast1 = fit1.forecast(12).rename("Model 1: Holt's linear trend\nAlpha=0.55, Beta=0.01")
#------------------------------------
# Holt model 2: alpha & beta Optimized
fit2 = Holt(series).fit(optimized=True)
fcast2 = fit2.forecast(12).rename("Model 2: Linear trend + optimized")

#=====================================
# Time and forecast plots 
#=====================================
series.plot(color='black', label='Original Data', legend=True)
#-------------------------------------
fit1.fittedvalues.plot(color='blue')
fcast1.plot(color='blue', legend=True)
#-------------------------------------
pyplot.xlabel('Years')
pyplot.ylabel('Values')
pyplot.title("Holt's method-based forecasts for Index of Production (K226)")
pyplot.show()
#-------------------------------------
series.plot(color='black', label='Original Data', legend=True)
#-------------------------------------
fit2.fittedvalues.plot(color='red')
fcast2.plot(color='red', legend=True)
#-------------------------------------
pyplot.xlabel('Years')
pyplot.ylabel('Values')
pyplot.title("Holt's method-based forecasts for Index of Production (K226)")
pyplot.show()

#====================================
# Evaluating the errors 
#====================================
from sklearn.metrics import mean_squared_error 
MSE1=mean_squared_error(fit1.fittedvalues, series)
MSE2=mean_squared_error(fit2.fittedvalues, series)

#=====================================
# Printing the paramters and errors of the methods
#=====================================
print('Summary of paramters and errors from each of the models:')
params = ['smoothing_level', 'smoothing_slope', 'damping_slope', 'initial_level', 'initial_slope']
results=pd.DataFrame(index=[r"alpha", r"beta", r"phi", r"l0", r"b0", "MSE"] ,columns=["Holt model 1", "Holt model 2"])
results["Holt model 1"] = [fit1.params[p] for p in params] + [MSE1]
results["Holt model 2"] = [fit2.params[p] for p in params] + [MSE2]

print(results)

#=====================================
# Evaluating and plotting the residual series for each scenario
#=====================================
residuals1= fit1.fittedvalues - series
residuals2= fit2.fittedvalues - series

residuals1.rename('residual plot for model 1').plot(color='red', legend=True)
residuals2.rename('residual plot for model 2').plot(color='blue', legend=True)

pyplot.title('Residual plots for models 1-2')
pyplot.show()

#=====================================
# ACF plots of the residual series for each scenario
#=====================================
from statsmodels.graphics.tsaplots import plot_acf
plot_acf(residuals1, title='Residual ACF for model 1', lags=50)
plot_acf(residuals2, title='Residual ACF for model 2', lags=50)
pyplot.show()