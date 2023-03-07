import datetime
import pandas as pd

## convert column to Data

df.index = pd.to_datetime(df.index)

# Convert Str to Date

df.index= datetime.datetime.strptime(df.index, '%Y-%m-%d').date()


# sum by Days 

date_1 = datetime.datetime.strptime(start_date, "%m/%d/%y")

end_date = date_1 + datetime.timedelta(days=10)