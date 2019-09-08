import pandas as pd 
import os  
import numpy as np 
 
df_huy = pd.read_csv("../Report/train_quora_features.tsv", error_bad_lines=False,delimiter='\t',encoding='utf-8')

print(df_huy.shape)
print(df_long.shape)