# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 08:14:24 2021

@author: lenovo
"""

from pandas import read_excel
from pandas import DataFrame
from numpy import sqrt
from numpy import log
from numpy import cbrt
import matplotlib.pyplot as plt

series = read_excel('EAFVdata_32049072.xlsx', sheet_name='CalAdj', header=0, squeeze=True)

OriginalData=series.Yt
CalAdj_OutlierPresent=series.Cal_adj
Data_OutlierRemoved=series.Outlier_adj_Yt
CalAdj_OutlierRemoved=series.Outlier_CalAdj

OriginalData.plot(label='Original series')
Data_OutlierRemoved.plot(label='Data_OutlierRemoved')
plt.legend()
plt.title('Time plot for EAFV data')
plt.show()

OriginalData.plot(label='Original series')
CalAdj_OutlierRemoved.plot(label='CalAdj_OutlierRemoved')

plt.title('Calendar adjustment for EAFV data')
plt.legend()
plt.title('Time plot for EAFV data')
plt.show()

CalAdj_OutlierRemoved.plot(label='CalAdj_OutlierRemoved')
plt.legend()
plt.title('Time plot for EAFV data')
plt.show()

plt.figure(1)
# line plot
plt.subplot(211)
plt.plot(CalAdj_OutlierRemoved)
plt.title('Time plot for EAFV data - Calendar Adjusted Outlier removed')
# histogram
plt.subplot(212)
plt.hist(CalAdj_OutlierRemoved)
plt.show()


#-----------------------
# Log transform for Calendar Adjusted and Outlier Removed Data
#-----------------------
dataframe1 = DataFrame(CalAdj_OutlierRemoved.values)
dataframe1.columns = ['EAFV']
dataframe1['EAFV'] = log(dataframe1['EAFV'])
plt.figure(1)
# line plot
plt.subplot(211)
plt.plot(dataframe1['EAFV'])
plt.title('Log transform-calendar adjusted Outlier removed EAFV')
# histogram
plt.subplot(212)
plt.hist(dataframe1['EAFV'])
plt.show()


#-----------------------
# Sqrt transform for Calendar Adjusted and Outlier Removed Data
#-----------------------
dataframe2 = DataFrame(CalAdj_OutlierRemoved.values)
dataframe2.columns = ['EAFV']
dataframe2['EAFV'] = sqrt(dataframe2['EAFV'])
plt.figure(1)
# line plot
plt.subplot(211)
plt.plot(dataframe2['EAFV'])
plt.title('Sqrt transform-calendar adjusted Outlier removed EAFV')
# histogram
plt.subplot(212)
plt.hist(dataframe2['EAFV'])
plt.show()

#-----------------------
# Cube Root transform for Calendar Adjusted and Outlier Removed Data
#-----------------------
dataframe2 = DataFrame(CalAdj_OutlierRemoved.values)
dataframe2.columns = ['EAFV']
dataframe2['EAFV'] = cbrt(dataframe2['EAFV'])
plt.figure(1)
# line plot
plt.subplot(211)
plt.plot(dataframe2['EAFV'])
plt.title('Cube root transform-calendar adjusted Outlier removed EAFV')
# histogram
plt.subplot(212)
plt.hist(dataframe2['EAFV'])
plt.show()

#-----------------------
# Negative Reciprocal transform for Calendar Adjusted and Outlier Removed Data
#-----------------------
dataframe2 = DataFrame(CalAdj_OutlierRemoved.values)
dataframe2.columns = ['EAFV']
dataframe2['EAFV'] = -1/(dataframe2['EAFV'])
plt.figure(1)
# line plot
plt.subplot(211)
plt.plot(dataframe2['EAFV'])
plt.title('Negative Reciprocal transform-calendar adjusted Outlier removed EAFV')
# histogram
plt.subplot(212)
plt.hist(dataframe2['EAFV'])
plt.show()