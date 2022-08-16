class Cliente:
    def __init__(self, nome, email, plano):
        self.nome = nome
        self.email = email
        self.lista_planos = ["basic", "premium"]
        if plano in self.lista_planos:
            self.plano = plano
        else:
            raise Exception("Plano invalido")


    def mudar_plano(self, novo_plano):
        if novo_plano in self.lista_planos:
            self.plano = novo_plano
        else:
            print("Plano invalido")


    def ver_filme(self, filme, plano_filme):
        if self.plano == plano_filme:
            print(f"Ver filme em 1080p {filme}")
        elif self.plano == "premium":
            print(f"Ver filme em 4K {filme}")
        elif self.plano == "basic" and plano_filme == "premium":
            print("Faça upgrate para premium para ver o filme em 4K ")
        else:
            print("plano invalido")



cliente = Cliente("Herbert", "herbert_galindo@hotmail.com", "premium")
print(cliente.plano)
cliente.ver_filme("Era do gelo", "basic")

cliente.mudar_plano("basic")
print(cliente.plano)
cliente.ver_filme("Era do gelo", "basic")
