# -*- coding: utf-8 -*-
"""
Created on Sat Apr 28 11:28:52 2018

@author: singh.shivam

"""
import numpy as np 
import pandas as pd
from pandas.tseries.offsets import *

X=np.array([7,2,0,3,4,2,5,0,3,4]);
izero = np.r_[-1, (X == 0).nonzero()[0]]  # indices of zeros
idx = np.arange(len(X))
Y=idx - izero[np.searchsorted(izero - 1, idx) - 1]
lst=list(zip(X,Y))
DF=pd.DataFrame(lst,columns=('X','Y'))
print('Step 1 :===Distance b/w zeros ===')
print(DF)

dateindex=pd.DatetimeIndex(start='2015-01-01',end='2015-12-31', freq=BusinessDay())
Randm=np.random.randint(1,len(dateindex),len(dateindex))
#lst =list(zip(dateindex,Randm))
New_df = pd.DataFrame(Randm,index=dateindex ,columns=['Values'])
print('Step 2 :============Date index of 2015 with random value ==========')
print(New_df.head())
New_df['Day'] = pd.to_datetime(New_df.index.values)
New_df['Day']=New_df['Day'].dt.weekday_name
wens=New_df.loc[New_df['Day']=='Wednesday']
sum_wedns_values=wens['Values'].sum()
print('Step 3:== Sum of values on wednesday==')
print(sum_wedns_values)
New_df['Month']=pd.to_datetime(New_df.index.values)
New_df['Month']=New_df['Month'].dt.month

Month_avg=[]
for i in range(1,13):
    month= New_df.loc[New_df['Month']==i]
    Month_avg.append(month['Values'].mean())

import calendar
#Converting the index to Month name 
New_df['Month'] = New_df['Month'].apply(lambda x: calendar.month_abbr[x])
Monthly_avg =pd.DataFrame(Month_avg,index=New_df['Month'].unique() ,columns=['Averages'])
print('Step 4:===Average of monthly values ===')
print(Monthly_avg)    
wens['Month']=pd.to_datetime(wens.index.values)
wens['Month']=wens['Month'].dt.month
print('Step 5:====Date of Max value in four consucutive months  =======')
for i in range(4,13,4):
    dumy= wens.loc[ (wens['Month']<i) & (wens['Month']>i-4)]
    print('Max in b/n',i-4,'and',i,'Months')
    print(dumy.loc[dumy['Values']==dumy['Values'].max()])
    print('==============================================')





 
