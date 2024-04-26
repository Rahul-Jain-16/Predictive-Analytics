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

series = read_excel('JQ2Jdata_32049072.xlsx', sheet_name='CalAdj', header=0, squeeze=True)

OriginalData = series.Yt
CalAdj_OutlierPresent = series.Cal_adj
Data_OutlierRemoved = series.Outlier_adj_Yt
CalAdj_OutlierRemoved = series.Outlier_CalAdj


OriginalData.plot(label='Original series')
CalAdj_OutlierPresent.plot(label='CalAdj_OutlierPresent')
plt.title('Time plot for JQ2J')
plt.legend()
plt.show()

OriginalData.plot(label='Original series')
CalAdj_OutlierRemoved.plot(label='CalAdj_OutlierRemoved')
plt.title('Calendar adjustment for JQ2J data')
plt.legend()
plt.show()

CalAdj_OutlierRemoved.plot(label='CalAdj_OutlierRemoved')
plt.title('Time plot for JQ2J')
plt.legend()
plt.show()

plt.figure(1)
# line plot
plt.subplot(211)
plt.plot(CalAdj_OutlierPresent)
plt.title('Time plot for JQ2J data - Cal-Adj Outlier_present')
# histogram
plt.subplot(212)
plt.hist(CalAdj_OutlierPresent)
plt.show()

plt.figure(1)
# line plot
plt.subplot(211)
plt.plot(CalAdj_OutlierRemoved)
plt.title('Time plot for JQ2J data - Cal-Adj Outlier_removed')
# histogram
plt.subplot(212)
plt.hist(CalAdj_OutlierRemoved)
plt.show()

#-----------------------
# Log transform
#-----------------------
dataframe1 = DataFrame(CalAdj_OutlierRemoved.values)
dataframe1.columns = ['JQ2J']
dataframe1['JQ2J'] = log(dataframe1['JQ2J'])
plt.figure(1)
# line plot
plt.subplot(211)
plt.plot(dataframe1['JQ2J'])
plt.title('Log transform-Cal_Adj Outlier_removed')
# histogram
plt.subplot(212)
plt.hist(dataframe1['JQ2J'])
plt.show()


#-----------------------
# Sqrt transform
#-----------------------
dataframe2 = DataFrame(CalAdj_OutlierRemoved.values)
dataframe2.columns = ['JQ2J']
dataframe2['JQ2J'] = sqrt(dataframe2['JQ2J'])
plt.figure(1)
# line plot
plt.subplot(211)
plt.plot(dataframe2['JQ2J'])
plt.title('Sqrt transform-Cal_Adj Outlier_removed')
# histogram
plt.subplot(212)
plt.hist(dataframe2['JQ2J'])
plt.show()

#-----------------------
# Cube Root transform
#-----------------------
dataframe2 = DataFrame(CalAdj_OutlierRemoved.values)
dataframe2.columns = ['JQ2J']
dataframe2['JQ2J'] = cbrt(dataframe2['JQ2J'])
plt.figure(1)
# line plot
plt.subplot(211)
plt.plot(dataframe2['JQ2J'])
plt.title('Cube root transform-Cal_Adj Outlier_removed')
# histogram
plt.subplot(212)
plt.hist(dataframe2['JQ2J'])
plt.show()

#-----------------------
# Negative Reciprocal transform
#-----------------------
dataframe2 = DataFrame(CalAdj_OutlierRemoved.values)
dataframe2.columns = ['JQ2J']
dataframe2['JQ2J'] = -1/(dataframe2['JQ2J'])
plt.figure(1)
# line plot
plt.subplot(211)
plt.plot(dataframe2['JQ2J'])
plt.title('Negative Reciprocal transform-Cal_Adj Outlier_removed')
# histogram
plt.subplot(212)
plt.hist(dataframe2['JQ2J'])
plt.show()