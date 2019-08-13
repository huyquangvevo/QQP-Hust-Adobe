import pandas as pd
import os 
import pandas as pd 
import numpy as np 
import tqdm

import gensim

df = pd.read_csv("./data/quora_duplicate_questions.tsv",delimiter='\t',encoding='utf-8')

df['question1'] = df['question1'].apply(lambda x: str(x))
df['question2'] = df['question2'].apply(lambda x: str(x))

# df['id'] = df['id'].apply(lambda x: str(x))

# df = df.loc[df['is_duplicate'] == 1]


list_q1 = list(df['question1'])
list_q2 = list(df['question2'])
id_pair = list(df['id'])

cols = ['id','qid1','qid2','question1','question2','is_duplicate']
# df_filter = pd.DataFrame(columns=list('id','qid1','qid2','question1','question2','is_duplicate'))
df_filter = pd.DataFrame()

count = 0

for id_ in range(len(list_q1)):
    q1 = str(list_q1[id_][:-1]).split()
    q2 = str(list_q2[id_][:-1]).split()
    q1 = sorted(q1)
    q2 = sorted(q2)
    if len(q1) == len(q2):
        is_equal = True
        for i in range(len(q1)):
            if q1[i] != q2[i]:
                is_equal = False
                break
        if is_equal:
            count += 1
            df_filter = df_filter.append(pd.DataFrame(df.loc[df['id'] == id_pair[id_]]),ignore_index=True)

print(count)
df_filter.to_csv('data/label_0and1_diff_order.tsv',index=False,sep='\t',encoding='utf-8')