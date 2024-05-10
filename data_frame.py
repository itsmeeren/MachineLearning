import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')
import numpy as np
# just create a dictionary
web_stat={'day':[15,54,75,85,48],
          'visitors':[57,85,95,68,41],
          'bus':[25,65,35,14,25]
        }# each and every key-pair in dictionary will be reflected as a column in dataframe
# converting this dictionary into data frame using pandas
df=pd.DataFrame(web_stat)# This will convert the entire dictionary set into the excel like sheet

# but for the number of the data mut be equal in each and every column
#print(df)
# can print required number using 
# print(df.head(2))
# print(df.tail(2))
#for setting the index 
#print(df.set_index('day'))
# setting an index creates another dataframe set but to avoid that

#df=df.set_index("day")
df.set_index('day',inplace=True)#this will modify the dataframe without changing the head
#to access the perticular column just use
#print(df.visitors)
#print(df['visitors'])
#If we want to reference two column

print(df[['visitors','bus']])
# for converting the a perticular column into the list

print(df.visitors.tolist())
# if more than one columns then use numpy
#his np.array() will convert multiple columns into the multidimensional array

print(np.array(df[['visitors','bus']]))
df.iloc[ : ,1:3]# for columns explicitely
df.iloc[ 1:3, : ] #for rows explicitely


