'''
Zip - Unindo iteráveis
Zip_longest - Itertools
'''

from itertools import zip_longest, count

indice = count()
cidades = ['São Paulo', 'Recife', 'Rio de Janeiro', 'Venturosa']
estados = ['SP', 'PE', 'RJ', 'PE']

cidades_estados = zip(
    indice,
    cidades,
    estados
)

for indice, cidades, estados in cidades_estados:
    print(indice,cidades,estados)