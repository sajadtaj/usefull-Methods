
#*------------------------------+
#*            encoding          |
#*------------------------------+
#* گرفتن خروجی که فایل تکست فارسی دارد
data_ebtal.to_csv('D:\data_ebtal.csv',encoding ='utf-8-sig')


## برای تبدیل اعداد و کارکتر های فارسی به انگلیسی 
df1['column'] = df1['column'].apply(unidecode)

## خواندن برخی دیتا های فارسی
# Method 1
pd.read_csv(r'D:\Tasks\Read csv file\10100047773.csv', sep='\t', encoding='utf-16')

# Method 2
with open(r'D:\Tasks\Read csv file\10100047773.csv', encoding='utf-16' ) as f:
    data = f.read()
    print(data)
