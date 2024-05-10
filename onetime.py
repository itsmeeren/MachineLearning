import pandas as pd
import numpy as np
import bottleneck as bt
import random
from sklearn.datasets import load_iris
from scipy.stats import linregress


import matplotlib.pyplot as plt


#creating the datraframe using predefined index using date_frame and HEAD AND TAIL functions
#
# index=pd.date_range('10/10/2025',periods=5)
# df=pd.DataFrame(np.random.randn(5,4),index=index,columns=list('WXYZ'))
# # print(df,df.tail(n=7),df.info())
# # print(df.info)
# # df.info()
# # print(df.__array__())
# pd.set_option('compute.use_bottleneck',False)
# print(df.to_numpy())

# idx=pd.Index(np.arange(10))
# print(idx)
# div,rem=divmod(idx,3)
# print(div,rem)
# print(df2)
# print(df1)
# print(df1.gt(df2))
# print(df2.gt(df1))
# print(np.nan==np.nan)# nan is not considered as number
# df1=pd.DataFrame(np.random.randn(3,3),columns=list('xyz'))
# df2=pd.DataFrame(np.random.randn(4,3),columns=list('xyz'))
# # df1.iloc[0,0]=np.nan
# print(df1)
# print(df1.describe())



# sd=pd.DataFrame([x for x in range(10)],columns=['features'])
# y=[random.randint(0,10) for x in range(10)]
# sd['target']=y
# # sd1=sd.set_index('x')
# print(sd1)
# corr_1=sd1['x'].corr(sd1['y'])
# print(corr_1)

# regression=linregress(sd['x'],sd['y'])
# print(regression)





# print(sd)
# sd['features']=np.nan
# print(sd)


# data_read=pd.read_csv('data2.csv',sep='|')
# print(data_read)
# f string allows the variables to be passed inside the string
# age='karthik'
# name='78'

# print_f=f"name is {name} and age is {age}"
# # print(print_f)
# import os

# # Execute a shell command
# os.system("sudo su")
# iris=load_iris()

# df=pd.DataFrame(iris.data,columns=iris.feature_names)
# print(df.shape)
# print(df.head)

x=pd.DataFrame({1:'apple',2:'apple',3:"banana"},index=list('W'))
print(x)
l=pd.factorize(x)[0]
print(l)

#Which assigns the value for the categories and helps in diffrentiating