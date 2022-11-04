#*------------------------------------+
#*      Find Value By == & isin       |
#*------------------------------------+

import pandas as pd
import numpy as np
df = pd.DataFrame({'num_legs': np.arange(0,100,.5), 'num_wings': np.random.random(200)})

x = df['num_legs'].isin(np.arange(1,100,1))
x_1 =df[df['num_legs']== 20]
x_2 = df[df['num_legs'].isin(np.arange(0,100,10))]
