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

series = read_excel('EAFVdata_32049072.xlsx', sheet_name = 'Data', header=0, index_col=0, parse_dates=True, squeeze=True) 

series.plot()

plt.xlabel('Year 1988-2020')
plt.ylabel("Monthly Index")
plt.title('Monthly Retail sales index, household goods, all businesses')
plt.show()

#------------------------------------------
#Time plot with histogram showing existing variance
#------------------------------------------

plt.figure(1)
# line plot
plt.subplot(211)
plt.plot(series)
plt.title('Time plot for EAFV data')
# histogram
plt.subplot(212)
plt.hist(series)
plt.show()

#------------------------------------------
#Square Root Tranformed time series plot
#------------------------------------------

dataframe1 = DataFrame(series.values)
dataframe1.columns = ['EAFV']
dataframe1['EAFV'] = sqrt(dataframe1['EAFV'])
plt.figure(1)
# line plot
plt.subplot(211)
plt.plot(dataframe1['EAFV'])
plt.title('Sqrt transform for EAFV data')
# histogram
plt.subplot(212)
plt.hist(dataframe1['EAFV'])
plt.show()

#------------------------------------------
#Log Tranformed time series plot
#------------------------------------------

dataframe1 = DataFrame(series.values)
dataframe1.columns = ['EAFV']
dataframe1['EAFV'] = log(dataframe1['EAFV'])
plt.figure(1)
# line plot
plt.subplot(211)
plt.plot(dataframe1['EAFV'])
plt.title('Log transform for EAFV data')
# histogram
plt.subplot(212)
plt.hist(dataframe1['EAFV'])
plt.show()

#------------------------------------------
#Cube Root Tranformed time series plot
#------------------------------------------

dataframe1 = DataFrame(series.values)
dataframe1.columns = ['EAFV']
dataframe1['EAFV'] = cbrt(dataframe1['EAFV'])
plt.figure(1)
# line plot
plt.subplot(211)
plt.plot(dataframe1['EAFV'])
plt.title('Cube root transform for EAFV data')
# histogram
plt.subplot(212)
plt.hist(dataframe1['EAFV'])
plt.show()

#------------------------------------------
#Negative Reciprocal Tranformed time series plot
#------------------------------------------

dataframe1 = DataFrame(series.values)
dataframe1.columns = ['EAFV']
dataframe1['EAFV'] = -1/(dataframe1['EAFV'])
plt.figure(1)
# line plot
plt.subplot(211)
plt.plot(dataframe1['EAFV'])
plt.title('Negative Reciprocal transform for EAFV data')
# histogram
plt.subplot(212)
plt.hist(dataframe1['EAFV'])
plt.show()