import pandas as pd 
from operator import xor
from sklearn.metrics import accuracy_score

df = pd.read_csv("../Report/bert_prediction_diff_mvsm.tsv",delimiter='\t',encoding='utf-8')

threshold = 1.0
alpha = 0.005

df_result = pd.DataFrame(columns=['threshold','examples','mis_classified','accuracy'])

df_prob_threshold = df.loc[df['BERT_probability']<=threshold]
df_prob_threshold = df_prob_threshold.loc[df_prob_threshold['BERT_probability']>(threshold - alpha)]


while not df_prob_threshold.empty:
    acc = accuracy_score(df_prob_threshold['is_duplicate'],df_prob_threshold['BERT_prediction'])
    # print("Threshold : %.2f" % threshold )
    # print("acc: %f" % acc)

    count = 0
    for index,row in df_prob_threshold.iterrows():
        if xor(bool(row['is_duplicate']),bool(row['BERT_prediction'])):
            count += 1
    
    df_result = df_result.append({'threshold':round(threshold,3),'examples':df_prob_threshold.shape[0],'mis_classified':count,'accuracy':acc},ignore_index=True)
    threshold -= alpha
    df_prob_threshold = df.loc[df['BERT_probability']<=threshold]
    df_prob_threshold = df_prob_threshold.loc[df_prob_threshold['BERT_probability']>(threshold - alpha)]


df_result.to_csv('../Report/threshold_proba_bert_prediction_on_diff_mvsm_alpha_005.tsv',index=False,sep='\t',encoding='utf-8')



#print(df_prob_threshold.shape)






# acc = (df_prob_threshold.shape[0] - count)/df_prob_threshold.shape[0]

# print("Examples : %d" % df_prob_threshold.shape[0])
# print("Mis: %d" % count)
# print("accuracy: %f" % acc)        

# df_prob_threshold.to_csv('../Report/threshold_proba_0.95_bert_prediction_on_dev.tsv',index=False,sep='\t',encoding='utf-8')
