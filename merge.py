#*------------------------------+
#*            Merge             |
#*------------------------------+
import pandas as pd

inner_merged_total = pd.merge(TradigMatch,
                                OrderBook,
                                how='left',
                                on=['key'],
                                suffixes=["_Trad","_Order"]  # For make diff each column with same names
                                )


## Merge many data frame with same length
# firs we merge alldata with df_0 to set lenth of alldata 
all_data =  df_0    
for i in (df_1,df_2,       ,df_n):  
    all_data = pd.merge(all_data,i, how='left',left_index=True, right_index=True )






## Merge Many DataFrame
# DataFrame in Dict
list_DataFrame =[df_1,df_2,df_3,df_4,df_5,df_6,df_7]
all_data=list_DataFrame[0]
for DATA in list_DataFrame[1:]:  
    all_data = pd.merge(all_data,DATA, how='left',on=['columns_A'])