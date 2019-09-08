import pandas as pd
import os 
import pandas as pd 
import numpy as np 
import tqdm

import gensim

df = pd.read_csv("../QQP/train.tsv",error_bad_lines=False,delimiter='\t',encoding='utf-8')
# df = pd.read_csv("../Report/BERT_LightGBM_prediction.tsv",delimiter='\t',encoding='utf-8')

df['question1'] = df['question1'].apply(lambda x: str(x))
df['question2'] = df['question2'].apply(lambda x: str(x))

# df['id'] = df['id'].apply(lambda x: str(x))

# df = df.loc[df['is_duplicate'] == 0]


list_q1 = list(df['question1'])
list_q2 = list(df['question2'])
id_pair = list(df['id'])

cols = ['id','qid1','qid2','question1','question2','is_duplicate']
# df_filter = pd.DataFrame(columns=list('id','qid1','qid2','question1','question2','is_duplicate'))
df_filter = pd.DataFrame()

count = 0

for id_ in range(len(list_q1)):
    q1 = str(list_q1[id_]).split()
    q2 = str(list_q2[id_]).split()
    i = 0
    if len(q1) == len(q2):
        continue
    len_min = min(len(q1),len(q2))
    while q1[i] == q2[i]:
        if i<len_min - 1:
            i+=1
        else:
            break
    
    j = 0
    while q1[len(q1) - 1 - j] == q2[len(q2) - 1 - j]:
        if j<len_min - 1:
            j+=1
        else:
            break
    if (i&j) & ((i+j)==(len_min - 1)):
        count += 1
        df_filter = df_filter.append(pd.DataFrame(df.loc[df['id'] == id_pair[id_]]),ignore_index=True)

print(count)
# df_filter.to_csv('../Report/bert_lightgbm_prediction_diff_1vsm.tsv',index=False,sep='\t',encoding='utf-8')