import pandas as pd
df=pd.concat(map(pd.read_csv,['dummy1.csv','dummy2.csv']),ignore_index=True)
print(df)
