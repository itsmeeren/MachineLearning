import pandas as pd
df=pd.read_csv('data2.csv')
# print(df )
df.set_index('Period',inplace=True)
df.to_csv('data_2_new.csv')
df2=pd.read_csv('data_2_new.csv')
# print(df2)

# We can redfine the columns of the csv file but the name should be given to each columns
df2.columns=['Karthik']
print(df2.head())
# if we dont want that name of the  columns then we can just add
df2.to_csv('data3.csv',header=False)

#Proper data conversion
df3=pd.read_csv('data3.csv',names=['xxx','yyy'],index_col=0)

#For renaming the columns
df3.rename(columns={'xxx':'yyy','zzz':'www'},inplace=True)


