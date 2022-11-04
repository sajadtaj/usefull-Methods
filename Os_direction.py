
#*------------------------------+
#*              OS              |
#*------------------------------+
from os import getcwd, path, makedirs

cwd = getcwd()      # 'گرفتن مسیر فعلی
Folder_Name = "folder name i"
Folder_Dir = path.join(cwd, Folder_Name)  # مشخص کردن ادرس 
makedirs(Folder_Dir, exist_ok=True) # ساخت مسیر مشخص شده
# اگر قبلا مسیر درست شده باشد دیگر نمی سازد



#**-------------------------------+
#*           relative path       |
#*  ساخت مسیر مادر در پروژه    |
#*-------------------------------+

import os
os.chdir(r'D:\Tranfer\Dashboards\Factor Investing')