Data = 'دیتابیس اصلی ما'
Factor_keys = ' مجموعه نام های که که میخواهیم به عنوان نام کلید وازه برگزینیم'
factore_dicts ={}
for i in Factor_keys:
    factore_dicts[i] = Data[Data['فیلتر مورد نظر'] == i]