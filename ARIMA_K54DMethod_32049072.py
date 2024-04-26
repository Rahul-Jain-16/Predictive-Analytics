# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 08:14:24 2021

@author: lenovo
"""

from pandas import read_excel
import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

weekly_earnings = read_excel('K54Ddata_32049072.xlsx', sheet_name = 'Data', header=0, index_col=0, parse_dates=True, squeeze=True)  # you can include various other parameters
weekly_earnings.plot()
plt.xlabel('Year 2000-2020')
plt.ylabel("Weekly Earnings in 1000'pounds")
plt.title('Monthly Average of private sector weekly pay')
plt.show()

# ACF plot on 50 time lags
plot_acf(weekly_earnings, title='ACF of Weekly Earnings time series', lags=50)

# PACF plot on 50 time lags
plot_pacf(weekly_earnings, title='PACF of weekly earnings time series', lags=50)
plt.show()

#  Seaonal difference
X = weekly_earnings.values
SeasDiff = list()
for i in range(12, len(X)):
	value = X[i] - X[i - 12]
	SeasDiff.append(value)
    
# Time, ACF, and PACF plots for the seasonally differenced series
plt.plot(SeasDiff)
plt.title('Time plot seasonally differenced series')
plot_acf(SeasDiff, title='ACF plot of seasonally differenced series', lags=50)
plot_pacf(SeasDiff, title='PACF plot of seasonally differenced series', lags=50)
plt.show()

### Seasonal + First difference
Y = SeasDiff
SeasFirstDiff = list()
for i in range(1, len(Y)):
	value = Y[i] - Y[i - 1]
	SeasFirstDiff.append(value)
plt.plot(SeasFirstDiff)
plt.title('Time plot seasonally + first differenced series')
plot_acf(SeasFirstDiff, title='ACF plot of seasonally + first differenced series', lags=50)
plot_pacf(SeasFirstDiff, title='PACF plot of seasonally + first differenced series', lags=50)
plt.show()