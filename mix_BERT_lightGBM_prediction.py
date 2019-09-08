import pandas as pd 
import os  
import numpy as np 
 
df = pd.read_csv("../QQP_DATA/QQP/dev.tsv", error_bad_lines=False,delimiter='\t',encoding='utf-8')
print(df.shape)

df_bert = pd.read_csv("../Report/bert_prediction_on_dev.tsv",error_bad_lines=False, delimiter='\t',encoding='utf-8')
df_lightGBM = pd.read_csv("../Report/LightGBM_prediction_original.tsv",delimiter='\t',encoding='utf-8')

df_bert['LightGBM_prediction'] = df_lightGBM['LightGBM_prediction']
df_bert['LightGBM_probability'] = df_lightGBM['LightGBM_probability']

# for index,row in df_bert.iterrows():
#     if row['LightGBM_prediction'] == 1:
#         print(row)

print(df_bert.shape)
print(df_bert.loc[df_bert['LightGBM_prediction'] == 1].shape)

# df_bert.astype({'LightGBM_prediction':'int32'})

df_bert.to_csv("../Report/BERT_LightGBM_prediction_original.tsv",index=False,sep='\t',encoding='utf-8')
