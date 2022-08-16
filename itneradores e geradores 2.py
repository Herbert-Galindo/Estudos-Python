nome = 'Herbert Galindo'
iterador = iter(nome)
gerador = (letra for letra in nome)

print(next(gerador))
print(next(gerador))
print(next(gerador))
print(next(gerador))
print(next(gerador))
print(next(gerador))
print(next(gerador))
print()
print('OLHA O FOR')

for letra in gerador:
    print(letra)

print('OLHA O OUTRO FOR')

for letra in gerador:
    print(letra)

print(next(gerador))

