file = open('Games.txt', 'w+')
file.write('The Witcher 3\n')
file.write('God of War\n')
file.write('Elden Ring\n')

file.seek(0, 0)
print('lendo linhas:')
print(file.read())
print('################\n')

file.seek(0, 0)
print(file.readline(), end='')
print(file.readline(), end='')
print(file.readline(), end='')
print('################\n')

file.seek(0, 0)
for linha in file:
    print(linha, end='')

file.close()