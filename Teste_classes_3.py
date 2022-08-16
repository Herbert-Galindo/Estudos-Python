class Carro:
    def __init__(self, marca, modelo, cor):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor

    def ligar(self):
        print("Ligando o motor")

    def acelerar(self):
        print("acelerando")

    def informacao(self):
        print(self.marca,self.modelo,self.cor)

carro1 = Carro(f"Fiat","Uno","Prata")
carro1.informacao()
carro1.ligar()
carro1.acelerar()
