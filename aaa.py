def Operacoes (X,Y):
    ad = X+Y
    su = X-Y
    mu = X*Y
    di = X/Y
    return ad,su,mu,di
print("inicio")
a = int(input("valor de a: "))
b = int(input("valor de b: "))
s = Operacoes(a,b)
print(s)