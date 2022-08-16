carrinho = []

carrinho.append(('Produto 1', 30))
carrinho.append(('Produto 2', 20))
carrinho.append(('Produto 3', 50))

total = sum([y for x, y in carrinho])           #Soma apenas dos valores contidos em Y (segunda coluna da tupla)
print(total)