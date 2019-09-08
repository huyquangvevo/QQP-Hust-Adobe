import pandas as pd 
import os  
import numpy as np 

f = open('../data/data_long_dev.txt','r')

columns = {"is_duplicate","feature1","feature2","feature3","feature4","feature5","feature6"}

df = pd.DataFrame(columns=["is_duplicate","feature1","feature2","feature3","feature4","feature5","feature6"])

count = 0

for line in f.readlines():
    features = line.split()
    count += 1
    print(count)
    df = df.append({'is_duplicate':features[1],'feature1':features[2],'feature2':features[3],'feature3':features[4],'feature4':features[5],'feature5':features[6],'feature6':features[7]},ignore_index=True)

f.close()

df.to_csv("../Report/long_features_dev.tsv",index=False,sep='\t',encoding='utf-8')