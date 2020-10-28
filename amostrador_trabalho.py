import pandas as pd


path = 'datasets\glass.txt'
df = pd.read_csv(path, delimiter=r'\t+',engine='python')

# utilizado para amostrar o dataset de diabetes
# df_sampled_positive = df[df['class'] == 'tested_positive'].sample(10, random_state = 42 )
# df_sampled_negative = df[df['class'] == 'tested_negative'].sample(10, random_state = 42 )

# df_sampled = df_sampled_positive.append(df_sampled_negative,ignore_index=True)
df_sampled = df.sample(20, random_state = 42 )

print(df_sampled)
df_sampled.to_csv('./glass_amostrado.txt',sep='\t',index=False)
