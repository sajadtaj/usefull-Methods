import pandas as pd
from datetime import datetime as dt

def convert_daytoweek(df:pd.DataFrame,day:str='Wednesday'):
    """This /function get daily Dataframe and convert this to weekly

    Args:
        df (pd.DataFrame): Dataframe must be include datatype column with name 'Date'
        day (str, optional): one day for start the week =('Sunday' 'Monday' 'Tuesday' 'Wednesday' 'Thursday' 'Friday' 'Saturday')

    Returns:
        Dataframe: Return weekly dataframe
    """
    index = df.index
    df.sort_index(inplace=True)
    start_day = df.index[0]
    end_day = df.index[len(df.index) - 1]

    Date =pd.date_range(start=start_day,end=end_day)
    Temp = pd.DataFrame({'Date':Date})
    merged = pd.merge(
        Temp,
        df,
        how='left',
        on= 'Date'
    )
    merged.ffill(axis=0,inplace=True)
    merged['weekDay']= merged['Date'].dt.day_name()
    finalDataframe =merged[merged['weekDay'] ==day ]

    return finalDataframe