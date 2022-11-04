#------------------------------+
#            selenium          |
#------------------------------+
from selenium import webdriver
import pandas as pd

driver = webdriver.Chrome(r'data\chromedriver.exe')
ask_df = pd.DataFrame()
df = pd.DataFrame()
"""
اطلاعات گرفته شده فقط مربوط به نماد های تابلو اصلی می باشد       
        http://www.tsetmc.com/loader.aspx?ParTree=111C1413&CComVal=NUMBER
        NUMBER برای گرفتن نماد های سایر تابلو ها باید آدرس بالا
باید تغییر یابد و متعاغبا مسیر یافتن امنت نیز بایست تغییر کند.       
"""

driver.get(f"http://www.tsetmc.com/loader.aspx?ParTree=111C1413&CComVal=1")

for d in range(1,160):
    for i in range(1,9):
        ask=driver.find_element_by_xpath(f'//*[@id="tblToGrid"]/tbody/tr[{d}]/td[{i}]')
        #Xpath
        ask_df[i] = pd.DataFrame([ask.text])
    df = pd.concat([df, ask_df], axis=0)
#*------------------------------+
#*              OS              |
#*------------------------------+
from os import getcwd, path, makedirs
os.h
cwd = getcwd()
Folder_Name = "Dictionary Stock"
Folder_Dir = path.join(cwd,Folder_Name)  # "....\Dictionary Stock"
makedirs(Folder_Dir, exist_ok=True) # ساخت مسیر ریشه


#*------------------------------+
#*    pprint  --> Dictionary    |
#*------------------------------+
"""
نمایش دیکشنری ب نحو مطلوب با پکیچ pprint
"""
from pprint import pprint as dicprint
# df_dict -> Dictionary
dicprint(df_dict)


#*------------------------------+
#*            pickle            |
#*------------------------------+

#* برای ذخیره کردن دیکشنری به حالت pickle
import pickle
with open(f'{Folder_Dir}\TabloAsli_Dictionary.pickle', 'wb') as handle:
    pickle.dump(df_dict, handle, protocol=pickle.HIGHEST_PROTOCOL)

#*#####
import pickle
#برای خوانن فایل pickle
with open(f'{Folder_Dir}\TabloAsli_Dictionary.pickle', 'rb') as handle:
    dict_a = pickle.load(handle)


df.to_pickle(rf'{Root_OB_Folder_Dir}\{Stock_Dict}_OrderBook\{Stock_Dict}_OB.pickle')


#*------------------------------+
#*            Tqdm              |
#*------------------------------+

import tqdm
import pandas as pd

for x in tqdm.tqdm(pd.date_range('2019-08-22', '2021-05-18', freq='1d')):
    print(x)

#*------------------------------+
#*            glob              |
#*------------------------------+
import glob
total_name_file = glob.glob("D:\Order Execution\execution\data\Json_data\Vghadir\OrderBook\*.pickle")

#*------------------------------+
#*        Excel Sheets          |
#*------------------------------+

#* خواندن شیت های یک اکسل
df1= pd.read_excel(r'D:\names.xlsx','نام شیت ')
df2= pd.read_excel(r'D:\names.xlsx','20101231-20151231')
df3 =pd.read_excel(r'D:\names.xlsx','20151231-20220523')
df4 =pd.read_excel(r'D:\names.xlsx','خرداد1401')


#*------------------------------+
#*            encoding          |
#*------------------------------+
#* گرفتن خروجی که فایل تکست فارسی دارد
data_ebtal.to_csv('D:\data_ebtal.csv',encoding ='utf-8-sig')


#*------------------------------+
#*            Drop Nan          |
#*------------------------------+
#* حذف کردن تمام Nan های درون دیتا فریم
df1.dropna()
df1['column'].dropna()


#*---------------------------------+
#*       Any Find : True & False   |
#*---------------------------------+
#* آیا درون این ردیف حتی یکی فالس وجود دارد؟
#* اگر حتی یک فالس داشتته باشد ترو برمیگرداند
df1['canceled'].any()

#*------------------------------+
#*            Merge             |
#*------------------------------+
inner_merged_total = pd.merge(TradigMatch,
                                OrderBook,
                                how='left',
                                on=['key']
                                )

#*------------------------------------+
#*      Find Value By == & isin       |
#*------------------------------------+

import pandas as pd
import numpy as np
df = pd.DataFrame({'num_legs': np.arange(0,100,.5), 'num_wings': np.random.random(200)})

x = df['num_legs'].isin(np.arange(1,100,1))
x_1 =df[df['num_legs']== 20]
x_2 = df[df['num_legs'].isin(np.arange(0,100,10))]


#*----------------------------------------+
#*    Find And Fill Position in Df        |
#*----------------------------------------+
import pandas as pd
import numpy as np
df = pd.DataFrame({'col_1': np.arange(0,100,.5), 'col_2': np.random.random(200) , 'col_3':np.arange(0,1000,5)})

raw10__col1 = df.loc[10,'col_1']
raw10_15__col1_col2 = df.loc[10:15 ,'col_1':'col_2']
raw10_end__col1 = df.loc[10:,'col_1']
#* Example

for i in range(len(df)):
    df.loc[i, 'col_1'] = 1-i




#*----------------------------------------+
#*                   MAP                  | 
#*          map(function, iterables)      |
#*----------------------------------------+
def myfunc(n):
    return len(n)
x = map(myfunc, ('apple', 'banana', 'cherry'))


def myfunc(a, b):
    return a + b

y = map(myfunc, ('apple', 'banana', 'cherry'), ('orange', 'lemon', 'pineapple'))
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



#**-------------------------------+
#*           relative path       |
#*  ساخت مسیر مادر در پروژه    |
#*-------------------------------+

import os
os.chdir(r'D:\Tranfer\Dashboards\Factor Investing')


#*---------------------------------------+
#*      بسته بندی 10 تای گردن داد ها    |
#*          تقسیم بسته ها به روز        |
#*---------------------------------------+
priods = 10
Data = 'دیتای اصلی ما'


total_pack =int(Data.shape[0] / priods)
total_pack
PacktData= Data.copy()
PacktData['packet'] = 'Nan'


#*      بسته بندی 10 تای گردن داد ها    
for i in range(0,total_pack):
    for d in range(0,priods): # days in each Periods
        PacktData.iloc[i * priods + d ,8] = i



Data['day of pack'] = 'Nan'
temp2=pd.DataFrame()
priods= 10
Data_temp = Data.copy()


#*          تقسیم بسته ها به روز        |
for pack in range(1,278):
    df = Data_temp[Data_temp['packet']==pack]
    for day in range(0,priods):
        df.iloc[day,9] = day + 1
    temp2 = pd.concat([temp2,df],axis=0)

Data_temp = temp2.copy()
Data_temp

#*------------------------------------------------------+
#* ساخت دیکشنری که هر ایتم آن یک دیتا بیس می باشد.   |
#*------------------------------------------------------+
Data = 'دیتابیس اصلی ما'
Factor_keys = ' مجموعه نام های که که میخواهیم به عنوان نام کلید وازه برگزینیم'
factore_dicts ={}
for i in Factor_keys:
    factore_dicts[i] = Data[Data['فیلتر مورد نظر'] == i]

#*------------------------------------------------------+
#*          پر کردن ستون دیتا فریم در حلقه            |
#*------------------------------------------------------+
Data = "دیتابیس که از قبل داریم"
for m in [2,3,15,20,25]:
    Data['position_%d' % m] = np.sign(Data['returns'].rolling(m).mean())
    Data['strategy_%d' % m] = (Data['position_%d' % m].shift(1) * Data['returns'])