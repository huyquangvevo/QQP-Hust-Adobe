import pandas as pd 
from operator import xor

df = pd.read_csv("./Report/bert_prediction_on_dev.tsv",delimiter='\t',encoding='utf-8')

df_mis = pd.DataFrame()

count = 0

for index, row in df.iterrows():
    if xor(bool(row['is_duplicate']),bool(row['BERT_prediction'])):
        df_mis = df_mis.append(df.iloc[[index]],ignore_index=True)
        count += 1

print(count)
df_mis.to_csv('./Report/misclassified_bert_prediction_on_dev.tsv',index=False,sep='\t',encoding='utf-8')
