#This is some useful options available in pandas from documentation

####__________________________________________####
import numpy as np
import pandas as pd
import random

date = pd.date_range('20240101', periods=3)
print(date)

date_df = pd.DataFrame(date, columns=['x'])
date_df.set_index('x',inplace=True)
date_df.to_csv('test.csv')
print(date_df)

# ifmore than one columns then i can give
new_data=pd.DataFrame(np.random.randn(6,4),columns=list('abcd'))# here the columns is defined by list

print(new_data)
# we can also use
merged=pd.merge(date_df,date_df,on='a',how='left')#inner and outer also be used
#like this also we can use other wise it only takes the  union

import pandas as pd

s=pd.Series(['hehe','fukyou'],[x for x in range(2)],name="fuck u")# using list comprehension
x=pd.DataFrame(s,columns=list('H'))
print(x)

#for handling arithamtic operation and filling nan values using fillna and Series format
df = pd.DataFrame(np.random.randn(10, 4), columns=["A", "B", "C", "D"])
df2 = pd.DataFrame(np.random.randn(7, 3), columns=["A", "B", "C"])
x=df.D
# print(pd.Series(x))
result_dataframe=df+df2
result_dataframe['D']=result_dataframe['D'].fillna(x)
print(result_dataframe)


#For creating the row data using pd.Series
s=pd.Series(['hehe','fukyou'],[x for x in range(2)],name="fuck u")# using list comprehension
print(s)
row_data = pd.Series({'A': 1, 'B': 2, 'C': 3, 'D': 4})
print(row_data)


# Using iloc integer loction function to create sub group or perticular rows or columns
s=pd.DataFrame(np.random.randn(10,3),columns=list('XYZ'))
print(s)


print(s.iloc[0:2,0:3]) # first slicing locates the range of rows to select here 2 is not included
                       # second one represents no of columns to be selected for subset creation

#For filling the values t0 a perticular row use iloc and assign the values from the list
s.iloc[0:1,0:3]=np.nan
s.iloc[0:1,0:3]=[1,2,3] #like this direct data can also be inserted


#While adding th3e dataframe use fill_values for
df1=pd.DataFrame(np.random.randn(3,3),columns=list('xyz'))
df2=pd.DataFrame(np.random.randn(4,3),columns=list('xyz'))
result=df1.add(df2,fill_value=1)
#this function is used to find the null values inside the function
pd.isna(df1)
# this function gives detailed description about the dataframe
df1.describe()


#common math formulas for the datas





####__________________________________________####