import pandas as pd

df = pd.DataFrame({'C1': [10, 11, 12], 'C2' : [20, 21, 22]}, index=[0, 1, 2])
df.to_hdf('test4.hdf5', key='df', mode='w')

read_df = pd.read_hdf('test4.hdf5')
print(read_df)