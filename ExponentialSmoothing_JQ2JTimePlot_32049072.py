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

series = read_excel('JQ2Jdata_32049072.xlsx', sheet_name = 'Data', header=0, index_col=0, parse_dates=True, squeeze=True) 

series.plot()

plt.xlabel('Year 2000-2020')
plt.ylabel("Turnover in million pounds")
plt.title('Time plot of Wholesale/retail trade Turnover (JQ2J) data')
plt.show()

#Time plot with histogram showing existing variance

plt.figure(1)
# line plot
plt.subplot(211)
plt.plot(series)
plt.title('Time plot for JQ2J data')
# histogram
plt.subplot(212)
plt.hist(series)
plt.show()

#------------------------------------------
#Square Root Tranformed time series plot
#------------------------------------------
dataframe1 = DataFrame(series.values)
dataframe1.columns = ['JQ2J']
dataframe1['JQ2J'] = sqrt(dataframe1['JQ2J'])
plt.figure(1)
# line plot
plt.subplot(211)
plt.plot(dataframe1['JQ2J'])
plt.title('Sqrt transform for JQ2J data')
# histogram
plt.subplot(212)
plt.hist(dataframe1['JQ2J'])
plt.show()

#------------------------------------------
#Log Tranformed time series plot
#------------------------------------------

dataframe1 = DataFrame(series.values)
dataframe1.columns = ['JQ2J']
dataframe1['JQ2J'] = log(dataframe1['JQ2J'])
plt.figure(1)
# line plot
plt.subplot(211)
plt.plot(dataframe1['JQ2J'])
plt.title('Log transform for JQ2J data')
# histogram
plt.subplot(212)
plt.hist(dataframe1['JQ2J'])
plt.show()

#------------------------------------------
#Cube Root Tranformed time series plot
#------------------------------------------

dataframe1 = DataFrame(series.values)
dataframe1.columns = ['JQ2J']
dataframe1['JQ2J'] = cbrt(dataframe1['JQ2J'])
plt.figure(1)
# line plot
plt.subplot(211)
plt.plot(dataframe1['JQ2J'])
plt.title('Cube root transform for JQ2J data')
# histogram
plt.subplot(212)
plt.hist(dataframe1['JQ2J'])
plt.show()

#------------------------------------------
#Negative Reciprocal Tranformed time series plot
#------------------------------------------

dataframe1 = DataFrame(series.values)
dataframe1.columns = ['JQ2J']
dataframe1['JQ2J'] = -1/(dataframe1['JQ2J'])
plt.figure(1)
# line plot
plt.subplot(211)
plt.plot(dataframe1['JQ2J'])
plt.title('Negative Reciprocal transform for JQ2J data')
# histogram
plt.subplot(212)
plt.hist(dataframe1['JQ2J'])
plt.show()

#------------------------------------------
#Time plot after removing outlier values
#------------------------------------------

series = read_excel('JQ2Jdata_32049072.xlsx', sheet_name = 'CalAdj', header=0, index_col=0, parse_dates=True, squeeze=True) 
series = series.Outlier_adj_Yt
series.plot()

plt.xlabel('Year 2000-2020')
plt.ylabel("Turnover in million pounds")
plt.title('Time plot of Wholesale/retail trade Turnover (JQ2J) data - Outlier adjusted')
plt.show()

#Time plot with histogram showing existing variance

plt.figure(1)
# line plot
plt.subplot(211)
plt.plot(series)
plt.title('Time plot for JQ2J data - Outlier adjusted')
# histogram
plt.subplot(212)
plt.hist(series)
plt.show()

#------------------------------------------
#Square Root Tranformed time series plot
#------------------------------------------
dataframe1 = DataFrame(series.values)
dataframe1.columns = ['JQ2J']
dataframe1['JQ2J'] = sqrt(dataframe1['JQ2J'])
plt.figure(1)
# line plot
plt.subplot(211)
plt.plot(dataframe1['JQ2J'])
plt.title('Sqrt transform for JQ2J data - Outlier adjusted')
# histogram
plt.subplot(212)
plt.hist(dataframe1['JQ2J'])
plt.show()

#------------------------------------------
#Log Tranformed time series plot
#------------------------------------------

dataframe1 = DataFrame(series.values)
dataframe1.columns = ['JQ2J']
dataframe1['JQ2J'] = log(dataframe1['JQ2J'])
plt.figure(1)
# line plot
plt.subplot(211)
plt.plot(dataframe1['JQ2J'])
plt.title('Log transform for JQ2J data - Outlier adjusted')
# histogram
plt.subplot(212)
plt.hist(dataframe1['JQ2J'])
plt.show()

#------------------------------------------
#Cube Root Tranformed time series plot
#------------------------------------------

dataframe1 = DataFrame(series.values)
dataframe1.columns = ['JQ2J']
dataframe1['JQ2J'] = cbrt(dataframe1['JQ2J'])
plt.figure(1)
# line plot
plt.subplot(211)
plt.plot(dataframe1['JQ2J'])
plt.title('Cube root transform for JQ2J data - Outlier adjusted')
# histogram
plt.subplot(212)
plt.hist(dataframe1['JQ2J'])
plt.show()

#------------------------------------------
#Negative Reciprocal Tranformed time series plot
#------------------------------------------

dataframe1 = DataFrame(series.values)
dataframe1.columns = ['JQ2J']
dataframe1['JQ2J'] = -1/(dataframe1['JQ2J'])
plt.figure(1)
# line plot
plt.subplot(211)
plt.plot(dataframe1['JQ2J'])
plt.title('Negative Reciprocal transform for JQ2J data - Outlier adjusted')
# histogram
plt.subplot(212)
plt.hist(dataframe1['JQ2J'])
plt.show()