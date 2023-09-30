import pandas as pd
import numpy as np
import os

df = pd.DataFrame()
# اگر دوتا ایندکس دارای که شامل تاریخ هم هست بهتر است آنها را مرتب کنی
df .set_index(['date','contract'],inplace=True)

df.sort_index(inplace=True)