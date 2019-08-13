import pandas as pd
import os 
import pandas as pd 
import numpy as np 
import tqdm

import gensim


df = pd.read_csv("./QQP/train.tsv",delimiter='\t',encoding='utf-8',error_bad_lines=False)

#df = df.drop(df.index[[18283]])
# df['is_duplicate'] = df['is_duplicate'].apply(lambda x: int(x))
#print(df.shape)
#d = list(df['is_duplicate'])
print(df.shape)

#for i in range(df.index);