
#*------------------------------------------------------+
#*          پر کردن ستون دیتا فریم در حلقه            |
#*------------------------------------------------------+

import pandas as pd


Data = "دیتابیس که از قبل داریم"
for m in [2,3,15,20,25]:
    Data['position_%d' % m] = np.sign(Data['returns'].rolling(m).mean())
    Data['strategy_%d' % m] = (Data['position_%d' % m].shift(1) * Data['returns'])