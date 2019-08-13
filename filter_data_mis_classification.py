import pandas as pd
import os 
import pandas as pd 
import numpy as np 
import tqdm

import gensim


df = pd.read_csv("./Report/mis_classified_bert_dev.tsv",delimiter='\t',encoding='utf-8')
fMis = open('./Report/result_lightgbm_true_on_bert_mis(dev).txt','r')


loc_data = pd.DataFrame()

count = 0

for i in range(df.shape[0]):
    l_item = int(fMis.readline())
    if l_item == 1:
        count += 1
        loc_data = loc_data.append(df.iloc[[i]],ignore_index=True)

loc_data.to_csv('./Report/lightgbm_true_on_mis_classified_bert_dev.tsv',index=False,sep='\t',encoding='utf-8')
fMis.close()
print("Mis Class: %d" % count)
