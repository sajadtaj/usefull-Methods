#*---------------------------------------+
#*      بسته بندی 10 تای گردن داد ها    |
#*          تقسیم بسته ها به روز        |
#*---------------------------------------+
import pandas as pd

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