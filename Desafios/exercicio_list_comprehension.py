string = '0123456789012345678901234567890123456789'
n = 10
lista = [string[c:c + n] for c in range(0, len(string), n)]
retorno = '.'.join(lista)
print(lista)
print(retorno)