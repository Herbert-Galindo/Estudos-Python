import pandas as pd

d = {
    'Produtos': ['Limão', 'Azeitona', 'Laranja'],
    'Quantidade': [12, 30, 26],
    'Preco': [25, 22, 50]
}

linhas_colunas = [1, 2, 3]

df = pd.DataFrame(data=d, index=linhas_colunas)
#print(df)
#produtos = df['Produtos']
#print(produtos)
#print(df.loc[3])

