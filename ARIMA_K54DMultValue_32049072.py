# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 12:32:33 2020

@author: abz1e14
"""
#1
#matplotlib inline
from pandas import read_excel
import matplotlib.pyplot as plt
import statsmodels.api as sm  
import warnings
import itertools
plt.style.use('fivethirtyeight')

df = read_excel('K54Ddata_32049072.xlsx', sheet_name = 'Data', header=0, index_col=0, parse_dates=True, squeeze=True)

#===================================================
#Identifying the parameters with smallest AIC
#===================================================
#Define the p, d and q parameters to take any value between 0 and 1
p = range(0, 2)
d = range(0, 2)
q = range(0, 2)

# Generate all different combinations of p, q and q triplets
pdq = list(itertools.product(p, d, q))

# Generate all different combinations of seasonal p, q and q triplets
seasonal_pdq = [(x[0], x[1], x[2], 12) for x in list(itertools.product(p, d, q))]

catch_param=[]
catch_seasonal = []
catch_aic = []
#print(len(pdq))
warnings.filterwarnings("ignore") # specify to ignore warning messages
catch = list()  
collectAICs=[]
for param in pdq:
    for param_seasonal in seasonal_pdq:
        try:
            mod = sm.tsa.statespace.SARIMAX(df,
                                            order=param,
                                            seasonal_order=param_seasonal,                                        
                                            enforce_invertibility=False)
            results = mod.fit()
            catch.append(results.aic)
            print('ARIMA{}x{} - AIC:{}'.format(param, param_seasonal, results.aic))
            catch_param.append(param)
            catch_seasonal.append(param_seasonal)
            catch_aic.append(results.aic)
            
        except:
            continue

import pandas as pd

df = pd.DataFrame({'param':catch_param,
                   'seasonal': catch_seasonal,
                   'aic': catch_aic})
writer = pd.ExcelWriter('Possible_Arima_combinations.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='Sheet1', index=False)
writer.save()

