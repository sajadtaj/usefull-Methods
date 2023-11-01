import datetime
import pandas as pd

## convert column to Data

df.index = pd.to_datetime(df.index)

# Convert Str to Date

df.index= datetime.datetime.strptime(df.index, '%Y-%m-%d').date()


# sum by Days 
date_1 = datetime.datetime.strptime(start_date, "%m/%d/%y")



end_date = date_1 + datetime.timedelta(days=10)


#-------------------------------------------------------------------
import jdatetime
# Convert Columns
# Convert 14020802 to  1402-08-02

def convert_to_new_format(date):
    year = int(str(date)[:4])
    month = int(str(date)[4:6])
    day = int(str(date)[6:8])
    persian_date = jdatetime.date(year, month, day)
    return persian_date.strftime("%Y-%m-%d")

Shasta_2['shamsiTradeDate'] = Shasta_2['shamsiTradeDate'].apply(convert_to_new_format)
