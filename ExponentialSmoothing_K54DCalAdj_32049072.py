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

series = read_excel('K54Ddata_32049072.xlsx', sheet_name='CalAdj', header=0, squeeze=True)

OriginalData=series.Yt
CalAdj_Data=series.Adjusted


OriginalData.plot(label='Original series')
CalAdj_Data.plot(label='Calendar Adjusted Data')
plt.legend()
plt.show()

CalAdj_Data.plot(label='CalAdj_Data')
plt.legend()
plt.show()

plt.figure(1)
# line plot
plt.subplot(211)
plt.plot(CalAdj_Data)
plt.title('Time plot for K54D data - Calendar Adjusted')
# histogram
plt.subplot(212)
plt.hist(CalAdj_Data)
plt.show()


#-----------------------
# Log transform
#-----------------------
dataframe1 = DataFrame(CalAdj_Data.values)
dataframe1.columns = ['K54D']
dataframe1['K54D'] = log(dataframe1['K54D'])
plt.figure(1)
# line plot
plt.subplot(211)
plt.plot(dataframe1['K54D'])
plt.title('Log transform-calendar adjusted K54D')
# histogram
plt.subplot(212)
plt.hist(dataframe1['K54D'])
plt.show()


#-----------------------
# Sqrt transform
#-----------------------
dataframe2 = DataFrame(CalAdj_Data.values)
dataframe2.columns = ['K54D']
dataframe2['K54D'] = sqrt(dataframe2['K54D'])
plt.figure(1)
# line plot
plt.subplot(211)
plt.plot(dataframe2['K54D'])
plt.title('Sqrt transform-calendar adjusted K54D')
# histogram
plt.subplot(212)
plt.hist(dataframe2['K54D'])
plt.show()

#-----------------------
# Cube Root transform
#-----------------------
dataframe2 = DataFrame(CalAdj_Data.values)
dataframe2.columns = ['K54D']
dataframe2['K54D'] = cbrt(dataframe2['K54D'])
plt.figure(1)
# line plot
plt.subplot(211)
plt.plot(dataframe2['K54D'])
plt.title('Cube root transform-calendar adjusted K54D')
# histogram
plt.subplot(212)
plt.hist(dataframe2['K54D'])
plt.show()

#-----------------------
# Negative Reciprocal transform
#-----------------------
dataframe2 = DataFrame(CalAdj_Data.values)
dataframe2.columns = ['K54D']
dataframe2['K54D'] = -1/(dataframe2['K54D'])
plt.figure(1)
# line plot
plt.subplot(211)
plt.plot(dataframe2['K54D'])
plt.title('Negative Reciprocal transform-calendar adjusted K54D')
# histogram
plt.subplot(212)
plt.hist(dataframe2['K54D'])
plt.show()