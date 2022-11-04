#*----------------------------------------------------------------+
#*     خواندن و ادغام مموعه از فایل های  پیکل با سرعت بالا      |
#**----------------------------------------------------------------+

import glob
import pandas as pd

total_name_file = glob.glob(r"D:\Order Execution\TSE PACK\ALL_ORDER_BOOKS\FEOLAD_OB\*.pickle")     #* حواندن نام فایل ها 

###* supar fast methods
total_data =[]
#* اغام تمام فایل ها در یک پیکل
for address in total_name_file : 
    df = pd.read_pickle(address)
    total_data.append(df)

## rare methods

total_data = pd.DataFrame()
for address in total_name_file : 
    df = pd.read_pickle(address)
    total_data = pd.concat([ total_data,df])

