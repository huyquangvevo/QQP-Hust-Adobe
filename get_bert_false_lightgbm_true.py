import pandas as pd 
from operator import xor

df = pd.read_csv("../Report/BERT_LightGBM_prediction_original.tsv",delimiter='\t',encoding='utf-8')

df_result = pd.DataFrame()

count = 0

for index, row in df.iterrows():
    if xor(bool(row['is_duplicate']),bool(row['BERT_prediction'])) and (not xor(bool(row['is_duplicate']),bool(row['LightGBM_prediction']))):
        df_result = df_result.append(df.iloc[[index]],ignore_index=True)
        count += 1

print(count)
df_result.to_csv('../Report/bert_false_lightgbm_true_on_dev.tsv',index=False,sep='\t',encoding='utf-8')
