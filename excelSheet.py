
#*------------------------------+
#*        Excel Sheets          |
#*------------------------------+

import pandas as pd

#* خواندن شیت های یک اکسل
df1= pd.read_excel(r'D:\names.xlsx','نام شیت ')
df2= pd.read_excel(r'D:\names.xlsx','20101231-20151231')
df3 =pd.read_excel(r'D:\names.xlsx','20151231-20220523')
df4 =pd.read_excel(r'D:\names.xlsx','خرداد1401')

#*------------------+
#*  Sheet names     |
#*------------------+

# Read All Sheets
file_name = pd.ExcelFile('Data.xlsx')
# Name of All Sheet
Sheet_names = file_name.sheet_names