# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 19:15:42 2020

@author: abz1e14
"""
from pandas import read_excel
import matplotlib.pyplot as plt
import numpy as np

series = read_excel('FTSEdata_32049072.xlsx', sheet_name='Train_set', header=0, 
                     squeeze=True, dtype=float)
 
correlval=np.corrcoef(series.FTSE, series.K54D)
correlval=correlval[1,0]
print(correlval)
correlval=np.corrcoef(series.FTSE, series.EAFV)
correlval=correlval[1,0]
print(correlval)
correlval=np.corrcoef(series.FTSE, series.K226)
correlval=correlval[1,0]
print(correlval)
correlval=np.corrcoef(series.FTSE, series.JQ2J)
correlval=correlval[1,0]
print(correlval)
correlval=np.corrcoef(series.K54D, series.EAFV)
correlval=correlval[1,0]
print(correlval)
correlval=np.corrcoef(series.K54D, series.K226)
correlval=correlval[1,0]
print(correlval)
correlval=np.corrcoef(series.K54D, series.JQ2J)
correlval=correlval[1,0]
print(correlval)
correlval=np.corrcoef(series.EAFV, series.K226)
correlval=correlval[1,0]
print(correlval)
correlval=np.corrcoef(series.EAFV, series.JQ2J)
correlval=correlval[1,0]
print(correlval)
correlval=np.corrcoef(series.K226, series.JQ2J)
correlval=correlval[1,0]
print(correlval)

