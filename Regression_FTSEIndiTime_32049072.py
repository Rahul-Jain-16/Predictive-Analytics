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
K226 = series.K226
JQ2J = series.JQ2J

#reading the indicator variables
D1=series.D1
D2=series.D2
D3=series.D3
D4=series.D4
D5=series.D5
D6=series.D6
D7=series.D7
D8=series.D8
D9=series.D9
D10=series.D10
D11=series.D11
time=series.time

#reading the time variable
time=series.time

#Regression model(s)

#formula = 'FTSE ~ K54D + EAFV + K226 + JQ2J+D1+D2+D3+D4+D5+D6+D7+D8+D9+D10+D11+time'

formula = 'FTSE ~ JQ2J + K54D + K226 + D3 + D8 +D9'

#Ordinary Least Squares (OLS)
results = ols(formula, data=series).fit()
print(results.summary())



