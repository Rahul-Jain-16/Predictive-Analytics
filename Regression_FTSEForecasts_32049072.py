# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 14:30:28 2020

@author: abz1e14
"""
from pandas import read_excel
from statsmodels.tsa.api import Holt
from statsmodels.tsa.api import ExponentialSmoothing
#from matplotlib import pyplot
import matplotlib.pyplot as plt
import numpy as np
from statsmodels.formula.api import ols
series = read_excel('FTSEdata_32049072.xlsx', sheet_name='Train_set', header=0, 
                     squeeze=True, dtype=float)

# Reading the basic variables
FTSE = series.FTSE
K54D = series.K54D
EAFV = series.EAFV
K226 = series.K226
JQ2J = series.JQ2J

trial_set_length = len(series)
set_forecast_period = 6

# Forecasting for AAA using Holt's linear method
fit1 = ExponentialSmoothing(K54D,trend='add', seasonal='mul',seasonal_periods = 12).fit(optimized=True)
fcast1 = fit1.forecast(set_forecast_period).rename("K54D_HWS_forecast")
fit1.fittedvalues.plot(color='red')
fcast1.plot(color='red', legend=True)
K54D.plot(color='black', legend=True)
plt.title('Forecast K54D with HWS')
plt.show()


# Forecasting for Tto4 using Holt's linear method
fit2 = ExponentialSmoothing(EAFV,trend='add', seasonal='mul',seasonal_periods = 12).fit(optimized=True)
fcast2 = fit2.forecast(set_forecast_period).rename("EAFV_HWS_forecast")
fit2.fittedvalues.plot(color='red')
fcast2.plot(color='red', legend=True)
EAFV.plot(color='black', legend=True)
plt.title('Forecast EAFV with HWS')
plt.show()

# Forecasting for D3to4 using Holt's linear method
fit3 = Holt(K226).fit(optimized=True)
#fit3 = Holt(D3to4).fit(optimized=True)
fcast3 = fit3.forecast(set_forecast_period).rename("K226_Holt_forecast")
fit3.fittedvalues.plot(color='red')
fcast3.plot(color='red', legend=True)
K226.plot(color='black', legend=True)
plt.title('Forecast EAFV with Holt-Linear')
plt.show()

# Forecasting for Tto4 using Holt's linear method
fit4 = ExponentialSmoothing(JQ2J,trend='add', seasonal='mul',seasonal_periods = 12).fit(optimized=True)
fcast4 = fit4.forecast(set_forecast_period).rename("JQ2J_HWS_forecast")
fit4.fittedvalues.plot(color='red')
fcast4.plot(color='red', legend=True)
JQ2J.plot(color='black', legend=True)
plt.title('Forecast JQ2J with HWS')
plt.show()

# Building the regression based forecast for main variable, DEOM
# Regression model(s)
formula = 'FTSE ~ JQ2J + K54D + K226 + D3 + D8 +D9'

# ols generate statistics and the parameters b0, b1, etc., of the model
results = ols(formula, data=series).fit()
results.summary()
b0 = results.params.Intercept
b1 = results.params.K54D
#b2 = results.params.EAFV
b3 = results.params.K226
b4 = results.params.JQ2J

# putting the fitted values of the forecasts of AAA, Tto4, and D3to4 in arrays
a1 = np.array(fit1.fittedvalues)
a2 = np.array(fit2.fittedvalues)
a3 = np.array(fit3.fittedvalues)
a4 = np.array(fit4.fittedvalues)

# Building the fitted part of the forecast of DEOM 
F=a1
for i in range(0,trial_set_length):
    F[i] = b0 + a1[i]*b1 + a3[i]*b3 + a4[i]*b4
#    F[i] = b0 + a1[i]*b1 + a2[i]*b2 + a3[i]*b3 + a4[i]*b4
    

# putting the values of the forecasts of AAA, Tto4, and D3to4 in arrays
v1=np.array(fcast1)
#v2=np.array(fcast2)
v3=np.array(fcast3)
v4=np.array(fcast4)

# Building the 6 values of the forecast ahead
E=v1
for i in range(0,set_forecast_period):
    E[i] = b0 + v1[i]*b1 + v3[i]*b3 + v4[i]*b4
#    E[i] = b0 + v1[i]*b1 + v2[i]*b2 + v3[i]*b3 + v4[i]*b4


# Joining the fitted values of the forecast and the points ahead
K=np.append(F, E)

# Reading the original DEOM time series for all the 59 periods
FTSEfull0 = read_excel('FTSEdata_32049072.xlsx', sheet_name='Full_data', header=0, squeeze=True, dtype=float)

###########################
# Evaluating the MSE to generate the confidence interval
FTSEfull = FTSEfull0.FTSE
values=FTSEfull[0:trial_set_length]
Error = values - F
MSE=(sum(Error**2))*1.0/len(F)

## Lower and upper bounds of forecasts for z=1.282; see equation (2.2) in Chap 2.
LowerE = E - 1.282*(MSE**(0.5))
UpperE = E + 1.282*(MSE**(0.5))

# LowerE = FTSEfull0.LowerE
# UpperE = FTSEfull0.UpperE
###############################

# Plotting the graphs of K and DEOMfull with legends
from matplotlib.legend_handler import HandlerLine2D
line1, = plt.plot(K, color='red', label='Forecast values')
line2, = plt.plot(FTSEfull, color='black', label='Original data')
line3, = plt.plot(LowerE, color='blue', label='Lower forecast')
line4, = plt.plot(UpperE, color='orange', label='Upper forecast')
plt.legend(handler_map={line1: HandlerLine2D(numpoints=4)})
plt.title('FTSE regression forecast with confidence interval')
plt.show()

# Proceeding as as in other demos, forecasts
# can be generated for other scenarios; i.e., with different combinations of variables


####*****************************
### NOW FORECASTING FOR THE WHOLE YEAR AFTER DEC 2020 TILL DEC 2021
####*****************************
series = read_excel('FTSEdata_32049072.xlsx', sheet_name='Train_set', header=0, 
                     squeeze=True, dtype=float)

FTSE = series.FTSE
K54D = series.K54D
EAFV = series.EAFV
K226 = series.K226
JQ2J = series.JQ2J

trial_set_length = len(series)
set_forecast_period = 12

# Forecasting for AAA using Holt's linear method
fit1 = ExponentialSmoothing(K54D,trend='add', seasonal='mul',seasonal_periods = 12).fit(optimized=True)
fcast1 = fit1.forecast(set_forecast_period).rename("K54D_HWS_forecast")
fit1.fittedvalues.plot(color='red')
fcast1.plot(color='red', legend=True)
K54D.plot(color='black', legend=True)
plt.title('Forecast K54D with HWS')
plt.show()


# Forecasting for Tto4 using Holt's linear method
fit2 = ExponentialSmoothing(EAFV,trend='add', seasonal='mul',seasonal_periods = 12).fit(optimized=True)
fcast2 = fit2.forecast(set_forecast_period).rename("EAFV_HWS_forecast")
fit2.fittedvalues.plot(color='red')
fcast2.plot(color='red', legend=True)
EAFV.plot(color='black', legend=True)
plt.title('Forecast EAFV with HWS')
plt.show()

# Forecasting for D3to4 using Holt's linear method
fit3 = Holt(K226).fit(optimized=True)
#fit3 = Holt(D3to4).fit(optimized=True)
fcast3 = fit3.forecast(set_forecast_period).rename("K226_Holt_forecast")
fit3.fittedvalues.plot(color='red')
fcast3.plot(color='red', legend=True)
K226.plot(color='black', legend=True)
plt.title('Forecast EAFV with Holt-Linear')
plt.show()

# Forecasting for Tto4 using Holt's linear method
fit4 = ExponentialSmoothing(JQ2J,trend='add', seasonal='mul',seasonal_periods = 12).fit(optimized=True)
fcast4 = fit4.forecast(set_forecast_period).rename("JQ2J_HWS_forecast")
fit4.fittedvalues.plot(color='red')
fcast4.plot(color='red', legend=True)
JQ2J.plot(color='black', legend=True)
plt.title('Forecast JQ2J with HWS')
plt.show()

# Building the regression based forecast for main variable, DEOM
# Regression model(s)
formula = 'FTSE ~ JQ2J + K54D + K226 + D3 + D8 +D9'

# ols generate statistics and the parameters b0, b1, etc., of the model
results = ols(formula, data=series).fit()
results.summary()
b0 = results.params.Intercept
b1 = results.params.K54D
#b2 = results.params.EAFV
b3 = results.params.K226
b4 = results.params.JQ2J

# putting the fitted values of the forecasts of AAA, Tto4, and D3to4 in arrays
a1 = np.array(fit1.fittedvalues)
a2 = np.array(fit2.fittedvalues)
a3 = np.array(fit3.fittedvalues)
a4 = np.array(fit4.fittedvalues)

# Building the fitted part of the forecast of DEOM 
F=a1
for i in range(0,trial_set_length):
    F[i] = b0 + a1[i]*b1 + a3[i]*b3 + a4[i]*b4
#    F[i] = b0 + a1[i]*b1 + a2[i]*b2 + a3[i]*b3 + a4[i]*b4
    

# putting the values of the forecasts of AAA, Tto4, and D3to4 in arrays
v1=np.array(fcast1)
#v2=np.array(fcast2)
v3=np.array(fcast3)
v4=np.array(fcast4)

# Building the 6 values of the forecast ahead
E=v1
for i in range(0,set_forecast_period):
    E[i] = b0 + v1[i]*b1 + v3[i]*b3 + v4[i]*b4
#    E[i] = b0 + v1[i]*b1 + v2[i]*b2 + v3[i]*b3 + v4[i]*b4


# Joining the fitted values of the forecast and the points ahead
K=np.append(F, E)

# Reading the original DEOM time series for all the 59 periods
FTSEfull0 = read_excel('FTSEdata_32049072.xlsx', sheet_name='Full_data', header=0, squeeze=True, dtype=float)

###########################
# Evaluating the MSE to generate the confidence interval

LowerE = E - 1.282*(MSE**(0.5))
UpperE = E + 1.282*(MSE**(0.5))

# LowerE = FTSEfull0.LowerE
# UpperE = FTSEfull0.UpperE
###############################

# Plotting the graphs of K and DEOMfull with legends
from matplotlib.legend_handler import HandlerLine2D
line1, = plt.plot(K, color='red', label='Forecast values')
line2, = plt.plot(FTSEfull, color='black', label='Original data')
line3, = plt.plot(LowerE, color='blue', label='Lower forecast')
line4, = plt.plot(UpperE, color='orange', label='Upper forecast')
plt.legend(handler_map={line1: HandlerLine2D(numpoints=4)})
plt.title('FTSE regression forecast with confidence interval')
plt.show()
