import pandas as pd
import numpy as np
#For concatenating the dataframe
df1=pd.DataFrame({
    "name": ["John", "Emily", "Michael", "Sophia", "Jacob"],
    "age": [25, 30, 35, 28, 40],
    "city": ["New York", "Los Angeles", "Chicago", "Houston", "Miami"],
    "gender": ["Male", "Female", "Male", "Female", "Male"],
    "salary": [50000, 60000, 70000, 55000, 80000]
})
df2=pd.DataFrame({
    "product_id": [101, 102, 103, 104, 105],
    "product_name": ["Laptop", "Smartphone", "Headphones", "Tablet", "Camera"],
    "category": ["Electronics", "Electronics", "Accessories", "Electronics", "Electronics"],
    "price": [1200, 800, 100, 500, 600],
    "stock_quantity": [50, 100, 200, 30, 80]
})

# concat=pd.concat([df1,df2])
# #print(concat)
# #for appending the dataframes
# df4=df1._append(df2)
# print(df4)

#If we want to append data serially use series function

s=pd.Series(['hehe',80,80,74,74],index= ['name','age','city','gender','salary'])
df5=df1._append(s,ignore_index=True)
# print(df5)

#for merging the database
web_stat_2 = {
    'day': [32, 54, 75, 85, 67],
    'visitors_2': [45, 82, 75, 68, 59],
    'bus_2': [20, 63, 32, 14, 27]
}

web2 = pd.DataFrame(web_stat_2)
web_stat={'day':[15,54,75,85,48],
          'visitors':[57,85,95,68,41],
          'bus':[25,65,35,14,25]
        }
web1=pd.DataFrame(web_stat)


# df6=pd.merge(web1.web2)
# print(df6)
#instead of this can use join also

web1.set_index('day',inplace=True)
web2.set_index('day',inplace=True)
joined=web1.join(web2)
print('joined data is',joined)




#for merging the database
# print(pd.merge(web1,web2,on='day'))

# to fill the datas whavinf the values nan
web1.fillna(value=5)# like this filled with values
pd.isna(web1)# by this boolean values is filled




