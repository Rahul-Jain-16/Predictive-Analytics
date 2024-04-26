# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 08:14:24 2021

@author: lenovo
"""

from pandas import read_excel
import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf
from pandas.plotting import autocorrelation_plot

series = read_excel('K226data_32049072.xlsx', sheet_name = 'Data', header=0, index_col=0, parse_dates=True, squeeze=True) 

series_1 = read_excel('K226data_32049072.xlsx', sheet_name = 'Seas_plot', header=0, index_col=0, parse_dates=True, squeeze=True) 

#---------------------
# Autocorrelation plot 
#---------------------

autocorrelation_plot(series)
plot_acf(series, title='ACF plot Index of Production (K226)-histogram format', lags=100)
plt.show()

'''
Autocorrelation plot shows smooth dying out of ACF values which shows that though there is coorelation between values, there is no seasonality in the data.
'''
#---------------------
# Seasonal plot 
#---------------------
series_1.plot()
plt.title('Seasonal plot for K226 data')
plt.show()

'''
Seasonal plot shows the seasonal trend does not follow the time series curve.
But this is not conclusive proof of seasonality. as shown above, ACF confirms that seasonality is absent in this data set.
'''

