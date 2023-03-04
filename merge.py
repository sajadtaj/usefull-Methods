#*------------------------------+
#*            Merge             |
#*------------------------------+
import pandas as pd

inner_merged_total = pd.merge(TradigMatch,
                                OrderBook,
                                how='left',
                                on=['key']
                                )


## Merge many data frame with same length
# firs we merge alldata with df_0 to set lenth of alldata 
all_data =  df_0    
for i in (df_1,df_2,       ,df_n):  
    all_data = pd.merge(all_data,i, how='left',left_index=True, right_index=True )

