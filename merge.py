#*------------------------------+
#*            Merge             |
#*------------------------------+
import pandas as pd

inner_merged_total = pd.merge(TradigMatch,
                                OrderBook,
                                how='left',
                                on=['key']
                                )
