import pandas as pd
import numpy as np
import quandl


data = quandl.get_table("AIER/AET", paginate=True,)
print(data)
df=pd.DataFrame()