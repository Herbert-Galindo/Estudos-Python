def divide(n1, n2):
    if n2 == 0:
        raise ValueError('n2 não pode ser zero')
        return n1 / n2
try:
    print(divide(n1=2,n2=0))
except ValueError as error:
    print('DIV 1:', error)
    print()

def number_convert(value):
    try:
        value = int(value)
        return value
    except ValueError:
        try:
            value = float(value)
            return value
        except ValueError:
            pass
while True:
    number = number_convert(input('DIV 2: Digite um numero: '))

    if number is None:
        print("ERROR: Isso não e um numero")
    else:
        print(number * 5)

