'''
Combinations, Permutations e Product  - Itertools
Combinação - Ordem não importa
Permutação - Ordem importa
Ambos não repetem valores únicos
Produto - Ordem importa e repete valores únicos
'''
from itertools import combinations, permutations, product

pessoas = ['Mayara', 'Herbert', 'Helder', 'Diogo', 'David']
for grupo in combinations(pessoas, 4):
    print(grupo)