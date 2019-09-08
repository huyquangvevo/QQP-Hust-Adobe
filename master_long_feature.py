import pandas as pd 
import os  
import numpy as np 

df = pd.read_csv("../Report/long_features_dev.tsv",delimiter='\t',encoding='utf-8')

df = df.astype({'is_duplicate':'int32','feature1':'float32','feature2':'float32','feature3':'float32','feature4':'float32','feature5':'float32','feature6':'float32'})

df.to_csv("../Report/long_features_dev_2.tsv",index=False,sep='\t',encoding='utf-8')

print(df.dtypes)
print(df.shape)
# for index,row in df.iterrows():
#     if row['is_duplicate']!=0.0 and row['is_duplicate'] != 1.0:
#         print(index)
#         print(row['is_duplicate'])


# print(df.dtypes)