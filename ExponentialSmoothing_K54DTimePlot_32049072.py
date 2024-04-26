# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 08:14:24 2021

@author: lenovo
"""

from pandas import read_excel
import matplotlib.pyplot as plt
from numpy import sqrt
from numpy import log
from numpy import cbrt
from pandas import DataFrame

series = read_excel('K54Ddata_32049072.xlsx', sheet_name = 'Data', header=0, index_col=0, parse_dates=True, squeeze=True) 

series.plot()

plt.xlabel('Year 2000-2020')
plt.ylabel("Monthly avg of Weekly earnings")
plt.title('Time series plot of Monthly average of private sector weekly pay')
plt.show()

#------------------------------------------
#Time plot with histogram showing existing variance
#------------------------------------------

plt.figure(1)
# line plot
plt.subplot(211)
plt.plot(series)
plt.title('Time plot for K54D data')
# histogram
plt.subplot(212)
plt.hist(series)
plt.show()

#------------------------------------------
#Square Root Tranformed time series plot
#------------------------------------------
dataframe1 = DataFrame(series.values)
dataframe1.columns = ['K54D']
dataframe1['K54D'] = sqrt(dataframe1['K54D'])
plt.figure(1)
# line plot
plt.subplot(211)
plt.plot(dataframe1['K54D'])
plt.title('Sqrt transform for K54D data')
# histogram
plt.subplot(212)
plt.hist(dataframe1['K54D'])
plt.show()

#------------------------------------------
#Log Tranformed time series plot
#------------------------------------------

dataframe1 = DataFrame(series.values)
dataframe1.columns = ['K54D']
dataframe1['K54D'] = log(dataframe1['K54D'])
plt.figure(1)
# line plot
plt.subplot(211)
plt.plot(dataframe1['K54D'])
plt.title('Log transform for K54D data')
# histogram
plt.subplot(212)
plt.hist(dataframe1['K54D'])
plt.show()

#------------------------------------------
#Cube Root Tranformed time series plot
#------------------------------------------

dataframe1 = DataFrame(series.values)
dataframe1.columns = ['K54D']
dataframe1['K54D'] = cbrt(dataframe1['K54D'])
plt.figure(1)
# line plot
plt.subplot(211)
plt.plot(dataframe1['K54D'])
plt.title('Cube root transform for K54D data')
# histogram
plt.subplot(212)
plt.hist(dataframe1['K54D'])
plt.show()

#------------------------------------------
#Negative Reciprocal Tranformed time series plot
#------------------------------------------

dataframe1 = DataFrame(series.values)
dataframe1.columns = ['K54D']
dataframe1['K54D'] = -1/(dataframe1['K54D'])
plt.figure(1)
# line plot
plt.subplot(211)
plt.plot(dataframe1['K54D'])
plt.title('Negative Reciprocal transform for K54D data')
# histogram
plt.subplot(212)
plt.hist(dataframe1['K54D'])
plt.show()