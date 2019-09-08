import pandas as pd 
# import numpy as np 
from sklearn.metrics import accuracy_score,f1_score

df = pd.read_csv("../Report/BERT_LightGBM_RULE.tsv", error_bad_lines=False,delimiter='\t',encoding='utf-8')

df = df.loc[df['rule'] == 0]

df.to_csv('../data/quora_rule.tsv',index=False,sep='\t',encoding='utf-8')
print(df.shape)