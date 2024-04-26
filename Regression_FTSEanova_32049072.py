# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 14:30:28 2020

@author: abz1e14
"""
from pandas import read_excel
from statsmodels.formula.api import ols
series = read_excel('FTSEdata_32049072.xlsx', sheet_name='Train_set', header=0, 
                     squeeze=True, dtype=float)

#reading the basic variables
FTSE = series.FTSE
K54D = series.K54D
EAFV = series.EAFV
K266 = series.K226
JQ2J = series.JQ2J

#Regression model(s)
formula = 'FTSE ~ K54D + EAFV + K266 + JQ2J'

#Ordinary Least Squares (OLS)
results = ols(formula, data=series).fit()
print(results.summary())

import numpy as np

 
# correlval=np.corrcoef(series.FTSE, series.K54D)
# correlval=correlval[1,0]
# print(correlval)
# correlval=np.corrcoef(series.FTSE, series.EAFV)
# correlval=correlval[1,0]
# print(correlval)
# correlval=np.corrcoef(series.FTSE, series.K226)
# correlval=correlval[1,0]
# print(correlval)
# correlval=np.corrcoef(series.FTSE, series.JQ2J)
# correlval=correlval[1,0]
# print(correlval)
# correlval=np.corrcoef(series.K54D, series.EAFV)
# correlval=correlval[1,0]
# print(correlval)
# correlval=np.corrcoef(series.K54D, series.K226)
# correlval=correlval[1,0]
# print(correlval)
# correlval=np.corrcoef(series.K54D, series.JQ2J)
# correlval=correlval[1,0]
# print(correlval)
# correlval=np.corrcoef(series.EAFV, series.K226)
# correlval=correlval[1,0]
# print(correlval)
# correlval=np.corrcoef(series.EAFV, series.JQ2J)
# correlval=correlval[1,0]
# print(correlval)
# correlval=np.corrcoef(series.K226, series.JQ2J)
# correlval=correlval[1,0]
# print(correlval)


# Here the main table is the first one,
# where the main statistics are the R-squared (line 1)
# and the P-value; i.e., Prob (F-statistic)