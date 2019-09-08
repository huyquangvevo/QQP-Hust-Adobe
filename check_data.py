import pandas as pd
import os 
import pandas as pd 
import numpy as np 
import tqdm

import gensim


df = pd.read_csv("../data/train_quora_features.tsv",delimiter='\t',encoding='utf-8',error_bad_lines=False)
print(df.shape)

for index,row in df.iterrows():
        if row['is_duplicate'] != 0.0 and row['is_duplicate'] != 1.0:
                df.loc[index,'is_duplicate'] = 0.0
                # row['is_duplicate'] = 0.0

# df = df.drop(df.index[[18283]])
df['is_duplicate'] = df['is_duplicate'].apply(lambda x: int(x))
print(df.shape)
df.to_csv('../Report/train_quora_features.tsv',index=False,sep='\t',encoding='utf-8')
# d = list(df['is_duplicate'])
# print(df.shape)

#for i in range(df.index);