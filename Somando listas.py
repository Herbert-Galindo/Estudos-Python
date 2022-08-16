'''
Considerando duas listas de inteiros ou floats (Lista A e Lista B)
Some os valores nas listas rertornando uma nova lista com os valores somados:

Se uma lista for maior que a outra, a soma só vai considerar o tamanho da
menor.

Exemplo:
lista_a         =[1, 2, 3, 4, 5, 6, 7]
lista_b         =[1, 2, 3, 4]

======================= Resultado
lista_soma = [2, 4, 6, 8]
'''


lista_a = [9, 8, 7, 6, 5, 4, 3]
lista_b = [1, 2, 3, 4]
lista_soma = [x + y for x,y in zip(lista_a, lista_b)]
print(lista_soma)
print()
print("_____________________________")
print()

'''
Opção 2
'''
from itertools import zip_longest

lista_a = [10, 2, 3, 4, 5]
lista_b = [12, 2, 3, 6, 50, 60, 70]
lista_soma = [x + y for x, y in zip_longest(lista_a, lista_b, fillvalue=0)]
print(lista_soma)  # [22, 4, 6, 10, 55, 60, 70]