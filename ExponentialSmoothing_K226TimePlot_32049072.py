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

series = read_excel('K226data_32049072.xlsx', sheet_name = 'Data', header=0, index_col=0, parse_dates=True, squeeze=True) 

series.plot()

plt.xlabel('Year 1997-2020')
plt.ylabel("Monthly Index")
plt.title(' Extraction of crude petroleum and natural gas.')
plt.show()

#------------------------------------------
#Time plot with histogram showing existing variance
#------------------------------------------

plt.figure(1)
# line plot
plt.subplot(211)
plt.plot(series)
plt.title('Time plot for K226 data')
# histogram
plt.subplot(212)
plt.hist(series)
plt.show()


#------------------------------------------
#Square Root Tranformed time series plot
#------------------------------------------
dataframe1 = DataFrame(series.values)
dataframe1.columns = ['K226']
dataframe1['K226'] = sqrt(dataframe1['K226'])
plt.figure(1)
# line plot
plt.subplot(211)
plt.plot(dataframe1['K226'])
plt.title('Sqrt transform for K226 data')
# histogram
plt.subplot(212)
plt.hist(dataframe1['K226'])
plt.show()

#------------------------------------------
#Log Tranformed time series plot
#------------------------------------------

dataframe1 = DataFrame(series.values)
dataframe1.columns = ['K226']
dataframe1['K226'] = log(dataframe1['K226'])
plt.figure(1)
# line plot
plt.subplot(211)
plt.plot(dataframe1['K226'])
plt.title('Log transform for K226 data')
# histogram
plt.subplot(212)
plt.hist(dataframe1['K226'])
plt.show()

#------------------------------------------
#Cube Root Tranformed time series plot
#------------------------------------------

dataframe1 = DataFrame(series.values)
dataframe1.columns = ['K226']
dataframe1['K226'] = cbrt(dataframe1['K226'])
plt.figure(1)
# line plot
plt.subplot(211)
plt.plot(dataframe1['K226'])
plt.title('Cube root transform for K226 data')
# histogram
plt.subplot(212)
plt.hist(dataframe1['K226'])
plt.show()

#------------------------------------------
#Negative Reciprocal Tranformed time series plot
#------------------------------------------

dataframe1 = DataFrame(series.values)
dataframe1.columns = ['K226']
dataframe1['K226'] = -1/(dataframe1['K226'])
plt.figure(1)
# line plot
plt.subplot(211)
plt.plot(dataframe1['K226'])
plt.title('Negative Reciprocal transform for K226 data')
# histogram
plt.subplot(212)
plt.hist(dataframe1['K226'])
plt.show()