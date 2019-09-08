import pandas as pd 
# import numpy as np 
from sklearn.metrics import accuracy_score,f1_score
import operator
from operator import xor

df = pd.read_csv("../Report/BERT_LightGBM_RULE.tsv", error_bad_lines=False,delimiter='\t',encoding='utf-8')
df_rule =  pd.read_csv("../data/quora_features_rule.tsv", error_bad_lines=False,delimiter='\t',encoding='utf-8')

df['entity1'] = df_rule['entity1']
df['entity2'] = df_rule['entity2']
df['time1'] = df_rule['time1']
df['time2'] = df_rule['time2']
df['url1'] = df_rule['url1']
df['url2'] = df_rule['url2']

# df = df.loc[operator.and_(df['BERT_prediction'], not operator.xor_(df['rule'],df['is_duplicate']))]
# df = df.loc[not operator.xor(df['rule'],df['is_duplicate']))]
# rule = df['rule']

df = df.loc[operator.and_(df['rule'] == 0, operator.and_(df['BERT_prediction'] == 1,df['is_duplicate'] == 0))]
# df = df.loc[operator.and_(df['BERT_prediction'],df['is_duplicate'])]
# df = df.loc[]

df.to_csv('../Report/rule_true.tsv',index=False,sep='\t',encoding='utf-8')
print("rule true classification")
print(df.shape)