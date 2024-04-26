# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 08:14:24 2021

@author: lenovo
"""

from pandas import read_excel
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.graphics.tsaplots import plot_acf
from pandas.plotting import autocorrelation_plot

series = read_excel('EAFVdata_32049072.xlsx', sheet_name = 'Data2', header=0, index_col=0, parse_dates=True, squeeze=True) 

series_1 = read_excel('EAFVdata_32049072.xlsx', sheet_name = 'Seas_plot', header=0, index_col=0, parse_dates=True, squeeze=True) 

#---------------------
# Autocorrelation plot 
#---------------------

autocorrelation_plot(series)
plot_acf(series, title='ACF plot Retail sales index-histogram format', lags=100)
plt.show()

'''
Autocorrelation plot shows spikes at lag 12,24,36 etc confirming presence of seasonality.
'''
#---------------------
# Seasonal plot 
#---------------------
series_1.plot()
plt.title('Seasonal plot for EAFV data')
plt.show()

'''
Seasonal plot shows the seasonal trend follows the time series curve.
This confirms our observation from the Time Plot that seasonality is multiplicative.
'''
#--------------------
# Seasonal decompose 
#--------------------

result = seasonal_decompose(series, model = 'multiplicative')
result.plot()
plt.show()

'''
Seasonal decompose with multiplicative seasonality shows the least residuals.
This confirms our observation from the Time Plot that seasonality is multiplicative.
'''