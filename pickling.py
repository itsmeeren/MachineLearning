import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
style.use('fivethirtyeight')

f1={'day':[15,54,75,85,48],
          'visitors':[57,85,95,68,41],
          'bus':[25,65,35,14,25]
        }
f2={'day':[14,55,45,85,48],
          'visitor':[55,8,989,65,46],
          'car':[25,6,3,14,5]
        }
x=pd.DataFrame(f1)
y=pd.DataFrame(f2)
x.to_pickle('x.pkl')
# y.to_pickle('y.pkl')

z=pd.read_pickle('x.pkl')
print(z)
#this is  how convertin the dataframe to a pickle file and read it back to get the dataframe



#before plotting the data its better to use pickle file format for easier plotting
z.plot()
# plt.legend().remove()#This will remove the namings in the  graph
# plt.show()

#For correlation
corr_matrix=z.corr()
# print(corr_matrix)

#IF correlation between the two specific columns is needed then use

corre_bus_visitors=z['bus'].corr(z['visitors'])
# print(corre_bus_visitors)

#Suppose if the data base have same values inside columun then for finding the reccurence pivot table is used
pivot_table=pd.pivot_table(z,values='bus',index=['visitors','day'])
print(pivot_table)
#this groupby function also helps finding repeated values inside a columns
grouped=z.groupby('bus').size()
# print(grouped)

#By series also we can construct data and then can be appended but  index should be ignored
s={'a':10,'b':11,'c':24,'d':80}
se=pd.Series(s)
s_d=pd.DataFrame(np.random.randn(3,3),columns=list('XYZ'))

print(se)
v=s_d._append(se,ignore_index=True)#only can
print(v)

# For reversing the any given string
reversed_s = s[::-1]
