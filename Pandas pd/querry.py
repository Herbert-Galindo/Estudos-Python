import pandas as pd
from numpy.random import rand

df = pd.DataFrame(rand(10,2), columns=list('ab'))
df.query('a > b')
print(df.query('a > b'))
print()

df = pd.DataFrame({'Produtos': ['Limão', 'Azeitona', 'Laranja'],
    'Quantidade': [12, 30, 26],
    'Preco': [25, 22, 50]})

print(df.query('Preco > Quantidade'))