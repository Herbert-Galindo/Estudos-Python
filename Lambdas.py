#Função tradicional
def funcao(arg, arg2):
    return arg * arg2

var = funcao(2,2)

#Lambdas
a = lambda x, y: x * y

list = [
    ["P1", 13],
    ["P2", 17],
    ["P3", 29],
    ["P4", 23],
]
print(sorted(list, key=lambda i: i[0], reverse=True))
print(list)