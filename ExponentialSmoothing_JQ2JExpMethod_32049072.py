# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 19:21:21 2020

@author: abz1e14
"""
from pandas import read_excel
import pandas as pd
from statsmodels.tsa.api import ExponentialSmoothing
from matplotlib import pyplot

def backTransform_CalAdj(forecast, fit_value, forecast_start=1):
    '''
        Parameters
    ----------
    forecast : insert Forecast values.
    fit_value : Insert fitted values of data set
    forecast_start : Month of forecast beginning, 1= January
        DESCRIPTION. The default is 1.

    Returns
    -------
    fit_value : Calendar adjustment removed from given fitted data .
    store_forecast_value : Calendar adjustment removed from given forecast values.
    '''
    days = [31,28,31,30,31,30,31,31,30,31,30,31]
    k=0
    
    for i in range(0,len(fit_value.fittedvalues)):
        fit_value.fittedvalues[i] = (fit_value.fittedvalues[i]*days[k]*12)/365.25
        if k<11:
            k+=1
        else:
            k=0
    
    store_forecast_value = forecast
    count = forecast_start-1
    for j in range(0,len(forecast)-1):
        store_forecast_value.values[j] = (store_forecast_value.values[j]*days[count]*12)/365.25
        if count <= 11:
            count+=1
        else:
            count=0

    return fit_value, store_forecast_value

series = read_excel('JQ2Jdata_32049072.xlsx', sheet_name='Data2', header=0, index_col=0, parse_dates=True, squeeze=True)

series2 = read_excel('JQ2Jdata_32049072.xlsx', sheet_name='CalAdj', header=0, index_col=0, parse_dates=True, squeeze=True)

org_series = series2.Outlier_adj_Yt

# ===================================
# Holt-Winter method in different scenarios # 
# ===================================
# ===================================
# Model 1: Holt-Winter method with additive trend and multiplicative seasonality 
# Here, alpha, beta, gamma are optimized
# ===================================
fit1 = ExponentialSmoothing(series, seasonal_periods=12, trend='add', seasonal='mul').fit()
new_fit1, new_forecast1 = backTransform_CalAdj(fit1.forecast(12), fit1, 1)

# ===================================
# Model 2: Holt-Winter method with additive trend and multiplicative seasonality and Damped values
# Here, the parameters alpha, beta, and gamma are optimized
# ===================================
fit2 = ExponentialSmoothing(series, seasonal_periods=12, trend='add', seasonal='mul', damped=True).fit()
new_fit2, new_forecast2 = backTransform_CalAdj(fit2.forecast(12), fit2, 1)

# ===================================
# Model 3: Holt-Winter method with additive trend and multiplicative seasonality
# Here, the parameters alpha = 0.4, beta = 0.0, and gamma = 0.3
# ===================================
fit3 = ExponentialSmoothing(series, seasonal_periods=12, trend='add', seasonal='mul').fit(smoothing_level = 0.31, smoothing_slope=0.05,  smoothing_seasonal=0.68)
new_fit3, new_forecast3 = backTransform_CalAdj(fit3.forecast(12), fit3, 1)

print("\n********************************\nForecasting Wholesale/Retail trade Turnover (K54D) with Holt-Winters method\n")
#=====================================
# Time and forecast plots
#=====================================


org_series.plot(label = 'Time plot of original series', legend=True)
new_forecast1.plot(label = 'Model 1: Opt HW-additive seasonality',color='red', legend=True)
new_fit1.fittedvalues.plot(color='red',legend=False)

pyplot.xlabel('Year')
pyplot.ylabel('Values')
pyplot.title('HW method-based forecasts for JQ2J Data')
pyplot.show()

org_series.plot(label = 'Time plot of original series', legend=True)
new_forecast2.plot(label = 'Model 2: Opt HW-additive seasonality_Damped',color='green', legend=True)
new_fit2.fittedvalues.plot(color='green')

pyplot.xlabel('Year')
pyplot.ylabel('Values')
pyplot.title('HW method-based forecasts for JQ2J Data')
pyplot.show()

org_series.plot(label = 'Time plot of original series', legend=True)
new_forecast3.plot(label = 'Model 3:\nHW-Multiplicative seasonality_\nAlpha=0.31,\nBeta=0.05,Gamma=0.68',color='green', legend=True)
new_fit3.fittedvalues.plot(color='green')

pyplot.xlabel('Year')
pyplot.ylabel('Values')
pyplot.title('HW method-based forecasts for JQ2J Data')
pyplot.show()
#====================================
# Evaluating the errors 
#====================================
from sklearn.metrics import mean_squared_error 
MSE1=mean_squared_error(new_fit1.fittedvalues, org_series)
MSE2=mean_squared_error(new_fit2.fittedvalues, org_series)
MSE3=mean_squared_error(new_fit3.fittedvalues, org_series)

#=====================================
# Printing the paramters and errors for each scenario
#=====================================
results=pd.DataFrame(index=[r"alpha", r"beta", r"gamma", r"l0", "b0", "MSE"])
params = ['smoothing_level', 'smoothing_slope', 'smoothing_seasonal', 'initial_level', 'initial_slope']
results["HW model 1"] = [new_fit1.params[p] for p in params] + [MSE1]
results["HW model 2"] = [new_fit2.params[p] for p in params] + [MSE2]
results["HW model 3"] = [new_fit3.params[p] for p in params] + [MSE3]
print(results)

#=====================================
# Evaluating and plotting the residual series for each scenario
#=====================================
residuals1= new_fit1.fittedvalues - org_series
residuals2= new_fit2.fittedvalues - org_series
residuals3= new_fit3.fittedvalues - org_series

residuals1.rename('residual plot for model 1').plot(color='red', legend=True)
residuals2.rename('residual plot for model 2').plot(color='blue', legend=True)
residuals3.rename('residual plot for model 3').plot(color='yellow', legend=True)

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
