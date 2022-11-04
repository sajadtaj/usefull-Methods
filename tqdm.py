
#*------------------------------+
#*            Tqdm              |
#*------------------------------+

import tqdm
import pandas as pd

for x in tqdm.tqdm(pd.date_range('2019-08-22', '2021-05-18', freq='1d')):
    print(x)