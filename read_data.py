import pandas as pd
import os 
import pandas as pd 
import numpy as np 
import tqdm

import gensim

# questions = pd.read_csv('./quora_duplicate_questions.tsv',delimiter='\t',encoding='utf-8')
# print(questions.head(35))

df = pd.read_csv("./QQP/dev.tsv",delimiter='\t')#,encoding='utf-8')

print(df.shape)

exit()
print("tiep")

df['question1'] = df['question1'].apply(lambda x: str(x))
df['question2'] = df['question2'].apply(lambda x: str(x))

df = df.loc[df['is_duplicate'] == 0]


list_q1 = list(df['question1'])
list_q2 = list(df['question2'])

# questions = list(df['question1']) + list(df['question2'])

print(list_q1[1] + "\n" + list_q2[1])

f = open('not_duplicate_question.txt','w')

threshold = 101

for i in range(1,threshold):
    if i==6:
        continue
    f.write(str(i) + '\n')
    f.write(list_q1[i] + '\n')
    f.write(list_q2[i] + '\n')

#print(df[0:100])

# questions = list(df['question1']) + list(df['question2'])
    

#print(questions)

#tokenize
# c = 0
# for question in tqdm(questions):
#     questions[c] = list(gensim.utils.tokenize(question,deacc=True,lower=True))
#     c += 1
# model = gensim.model.Word2Vec(questions,size=300,workers=16,iter=10,negative=20)