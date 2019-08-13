import pandas as pd
import os 
import pandas as pd 
import numpy as np 
import tqdm

import gensim

df = pd.read_csv("./quora_duplicate_questions.tsv",delimiter='\t',encoding='utf-8')

df['question1'] = df['question1'].apply(lambda x: str(x))
df['question2'] = df['question2'].apply(lambda x: str(x))

# df['id'] = df['id'].apply(lambda x: str(x))

df = df.loc[df['is_duplicate'] == 0]


list_q1 = list(df['question1'])
list_q2 = list(df['question2'])
id_pair = list(df['id'])

cols = ['id','qid1','qid2','question1','question2','is_duplicate']
# df_filter = pd.DataFrame(columns=list('id','qid1','qid2','question1','question2','is_duplicate'))
df_filter = pd.DataFrame()
# df_filter = df_filter.append(pd.DataFrame(df.loc[df['id'] == id_pair[0]]),ignore_index=True)

# d = pd.DataFrame(df.loc[df['id'] == 11])
# df_filter = df_filter.append(d,ignore_index=True)

# print(df_filter.count())

# df_filter.to_csv('df_filter_data.csv',sep='\t',encoding='utf-8')


# f = open('sample2_data_label_1.txt','w', encoding='utf-8')

count = 0

for id_ in range(len(list_q1)):
    q1 = str(list_q1[id_]).split()
    q2 = str(list_q2[id_]).split()
    i = 0
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
    if (i&j) & (i+j==len_min - 1):
        count += 1
        #print(id_pair[id_])
        df_filter = df_filter.append(pd.DataFrame(df.loc[df['id'] == id_pair[id_]]),ignore_index=True)
        break
        # f.write((id_pair[id_]) + '\n')
        # f.write(list_q1[id_] + '\n')
        # f.write(list_q2[id_] + '\n')

# f.close()

# data for sample_data_label_1.tsv
#df_filter.to_csv('sample_data_label_1.tsv',index=False,sep='\t',encoding='utf-8')

# data for sample2_data_label_1.tsv
#df_filter.to_csv('sample2_data_label_1.tsv',index=False,sep='\t',encoding='utf-8')

# data for sample_data_label_0.tsv
#df_filter.to_csv('sample_data_label_0.tsv',index=False,sep='\t',encoding='utf-8')

# data for sample2_data_label_0.tsv
#df_filter.to_csv('sample2_data_label_0.tsv',index=False,sep='\t',encoding='utf-8')

# data for sample2_data_label_0.tsv
df_filter.to_csv('test_sample2_data_label_0.tsv',index=False,sep='\t',encoding='utf-8')

# print(count)