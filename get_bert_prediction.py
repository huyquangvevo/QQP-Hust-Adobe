import pandas as pd 
from operator import xor

df_data = pd.read_csv("./QQP/dev.tsv",delimiter='\t',encoding='utf-8')
df_prediction = pd.read_csv("./Report/bert_prediction_on_dev_proba.tsv",delimiter='\t',encoding='utf-8')

df_data['BERT_prediction'] = df_prediction['BERT_prediction']
df_data['BERT_probability'] = df_prediction['BERT_probability']

# df_mis = pd.DataFrame()

# count = 0

# for index, row in df_data.iterrows():
#     if xor(bool(row['is_duplicate']),bool(row['BERT_prediction'])):
#         df_mis = df_mis.append(row,ignore_index=True)
#         count += 1

# print(count)
# df_mis.to_csv('./Report/misclassified_bert_prediction_on_dev.tsv',index=False,sep='\t',encoding='utf-8')

df_data.to_csv('./Report/bert_prediction_on_dev.tsv',index=False,sep='\t',encoding='utf-8')

