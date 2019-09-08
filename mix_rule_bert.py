import pandas as pd 


df = pd.read_csv("../Report/BERT_LightGBM_prediction_original.tsv", error_bad_lines=False,delimiter='\t',encoding='utf-8')
df_rule = pd.read_csv("../data/quora_features_long.tsv",error_bad_lines=False, delimiter='\t',encoding='utf-8')

# print(df.shape)
# print(df_rule.shape)

df['rule'] = df_rule['rule']

# rule = df_rule['rule']
# bert = df['BERT_prediction']


# df['BERT_Rules'] = df['BERT_Rules'].apply(lambda df: df['BERT_Rules'] and df['BERT_prediction'])

df.to_csv("../Report/BERT_LightGBM_RULE.tsv",index=False,sep='\t',encoding='utf-8')
