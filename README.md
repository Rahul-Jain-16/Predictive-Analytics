# Predictive-Analytics
PYTHON: Data cleaning, transformation, manipulation, modeling, visualisation, linear regression, multivariate regression, ARIMA

**Background:** 
The report is to forecast the behaviour of a number of key economic indicators until December 2021; the relevant data sets are to be obtained from the UK Government Oce for National Statistics (ONS{for short) website. A recommendation is sought as to whether these economic indicators can be used to forecast the FTSE 100 Financial Times Index itself, in the context of the ongoing economic crisis.

**Data Introduction:**
5 input files:
1. K54D = Monthly Average of private sector weekly pay
2. EAFV = Retail sales index, household goods, all businesses
3. K226 = Extraction of crude petroleum and natural gas
4. JQ2J = The manufacturing and business sector of Great Britain, total turnover and orders.
5. FTSE = FTSE 100 index

**File naming conventions:**
All python files follow the same naming convention which is <forecasting method>_<data><cleaning or transformation used>_<UID>. For example, Regression_FTSEForecasts_32049072.py means regression techniques were used on the FTSE dataset, where FTSE is the dependent variable and other 4 datasets were independent, and it forecasts the index (i.e. dependent variable). For exponential smoothing methods, data cleaning, transformations, any calendar adjustments were done in individual files. 

**Please read the "TechnicalReport_32049072.pdf" for details about the methodology and results.** Please note that a defined reporting format was mandated and hence all graphs are located towards the end of the report.

