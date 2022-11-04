#*----------------------------------------+
#*    Find And Fill Position in Df        |
#*----------------------------------------+
import pandas as pd
import numpy as np

df = pd.DataFrame(
    {'col_1': np.arange(0,100,.5),
    'col_2': np.random.random(200) ,
    'col_3':np.arange(0,1000,5)}
  )

raw10__col1 = df.loc[10,'col_1']
raw10_15__col1_col2 = df.loc[10:15 ,'col_1':'col_2']
raw10_end__col1 = df.loc[10:,'col_1']
#* Example

for i in range(len(df)):
    df.loc[i, 'col_1'] = 1-i