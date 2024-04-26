# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 10:56:03 2020

@author: abz1e14
"""
from pandas import read_excel
from statsmodels.tsa.api import SimpleExpSmoothing
from statsmodels.tsa.api import Holt
from statsmodels.tsa.api import ExponentialSmoothing
from matplotlib import pyplot
series = read_excel('K226data_32049072.xlsx', sheet_name='Data', header=0, index_col=0, parse_dates=True, squeeze=True)
length = len(series)
test_set = series[:length-6]
train_set = series[-6:]

# ==============================
# Simple Exponential Smoothing #
# ==============================
## SES model 1: alpha = 0.5
fit1 = SimpleExpSmoothing(test_set).fit(optimized=True)
fcast1 = fit1.forecast(6).rename(r'$\alpha=%s$'%fit1.model.params['smoothing_level'])
# Plot of fitted values and forecast of next 6 values, respectively
fit1.fittedvalues.plot(color='blue')
fcast1.plot(color='blue', legend=True)

series.plot(color='yellow', legend=True)
pyplot.xlabel('Dates')
pyplot.ylabel('Values')
pyplot.title('SES method-based forecasts for K226 data')
pyplot.show()

# Holt model 2: alpha & beta Optimized
fit2 = Holt(test_set).fit(optimized=True)
fcast2 = fit2.forecast(6).rename("Model 2: Linear trend + optimized")
fit2.fittedvalues.plot(color='red')
fcast2.plot(color='red', legend=True)

series.plot(color='yellow', legend=True)
pyplot.xlabel('Dates')
pyplot.ylabel('Values')
pyplot.title('SES method-based forecasts for K226 data')
pyplot.show()

fit3 = ExponentialSmoothing(test_set, seasonal_periods=12, trend='add', seasonal='mul').fit()
fcast3 = fit3.forecast(6).rename("Model 3: Holt Winter Seasonal")
fit3.fittedvalues.plot(color='blue')
fcast3.plot(color='red', legend=True)

series.plot(color='yellow', legend=True)
pyplot.xlabel('Dates')
pyplot.ylabel('Values')
pyplot.title('SES method-based forecasts for K226 data')
pyplot.show()


# Plotting the original data together with the 3 forecast plots

def MSE_forecast(fcast, train_set):
    total = 0
    for i in range(0, len(train_set)):
        num = (fcast[i] - train_set[i])**2
        total+=num
    MSE = total / len(train_set)
    return MSE
    
MSE1 = MSE_forecast(fcast1, train_set)
MSE2 = MSE_forecast(fcast2, train_set)
MSE3 = MSE_forecast(fcast3, train_set)

print('\nSummary of errors resulting from models 1, 2 & 3:')
import pandas as pd
cars = {'Model': ['MSE'],
        'SES model': [MSE1],
        'Holt-Linear model': [MSE2],
        'HW model': [MSE3]
        }
AllErrors = pd.DataFrame(cars, columns = ['Model', 'SES model', 'Holt-Linear model', 'HW model'])
print(AllErrors)
