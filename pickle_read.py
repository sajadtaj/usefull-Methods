#*------------------------------+
#*            pickle            |
#*------------------------------+

#* برای ذخیره کردن دیکشنری به حالت pickle
import pickle
with open(f'{Folder_Dir}\TabloAsli_Dictionary.pickle', 'wb') as handle:
    pickle.dump(df_dict, handle, protocol=pickle.HIGHEST_PROTOCOL)

#*#####
import pickle
#برای خوانن فایل pickle
with open(f'{Folder_Dir}\TabloAsli_Dictionary.pickle', 'rb') as handle:
    dict_a = pickle.load(handle)

# برای ذخیره کردن
df.to_pickle(rf'{Root_OB_Folder_Dir}\{Stock_Dict}_OrderBook\{Stock_Dict}_OB.pickle')

