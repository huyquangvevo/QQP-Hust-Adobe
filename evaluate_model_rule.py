import pandas as pd 
import numpy as np 
from sklearn.metrics import accuracy_score,f1_score

df = pd.read_csv("../Report/BERT_LightGBM_RULE.tsv", error_bad_lines=False,delimiter='\t',encoding='utf-8')

bert = df['BERT_prediction']
rule = df['rule']
result_br = np.bitwise_and(bert,rule)
label = df['is_duplicate']
# print(result_br)
print("Mix BERT and Rule")
print('Accuracy score: %f' % accuracy_score(label,result_br))
print('F1 score: %f' % f1_score(label,result_br))

print('Mix BERT and LightGBM')
light = df['LightGBM_prediction']
result_bl = np.bitwise_and(bert,light)
print('Accuracy score: %f' % accuracy_score(label,result_bl))
print('F1 score: %f' % f1_score(label,result_bl))