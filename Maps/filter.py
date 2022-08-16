from dados import produtos, pessoas, lista


def filtra(produto):
    if produto['preco'] > 50:
        produto['Maior que R$ 50'] = True
        return True

nova_lista = filter(filtra, produtos)

for produto in nova_lista:
    print(produto)



