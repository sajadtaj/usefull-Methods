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