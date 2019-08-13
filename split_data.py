import sys
import os 
import pandas as pd 
import numpy as np 
from tqdm import tqdm 
import gensim
from gensim.models import Word2Vec
from sklearn.model_selection import train_test_split
# questions = pd.read_csv('./quora_duplicate_questions.tsv',delimiter='\t',encoding='utf-8')
# print(questions.head(35))
df = pd.read_csv("./data/quora_duplicate_questions.tsv",delimiter='\t', encoding='utf-8')

X_train = pd.DataFrame()
X_test = pd.DataFrame()

X_train, X_test = train_test_split(df ,test_size=0.33, random_state=42)

X_test.to_csv('./data/test.tsv',index=False,sep='\t',encoding='utf-8')



