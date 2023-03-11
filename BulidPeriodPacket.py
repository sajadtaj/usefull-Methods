import pandas as pd

def BuildPeriodPack(data:pd.DataFrame, periods :int= 10):
    """Get Data and split this in periods packs for ex:
    2500 Data & 10 periods -> 250 pack

    Args:
        data (pd.DataFrame): DataFrame
        periods (int, optional): periods of pack

    Returns:
        dataFrame that split to packet with periods day
    """
    # caculate data.shpe / period
    PacktData = data.copy()
    total_pack = int(PacktData.shape[0] / periods )

    # build packet 
    PacktData['packet'] = 'Nan'
    # fill 'packet' col
    PacketIndex = PacktData.columns.get_loc('packet')
    for i in range(0,total_pack):
        for d in range(0,periods): # days in each Periods
            PacktData.iloc[i * periods + d ,PacketIndex] = i

    # build days for each pack 
    PacktData['day of pack'] = 'Nan'
    DayOfPackIndex = PacktData.columns.get_loc('day of pack')
    resultData=pd.DataFrame()

    # fill 'day of pack' col
    for pack in range(1,total_pack):
        df = PacktData[PacktData['packet']==pack]
        for day in range(0,periods):
            df.iloc[day,DayOfPackIndex] = day + 1
        resultData = pd.concat([resultData,df],axis=0)

    return resultData

