class Console:
    def __init__(self, marca, modelo, cor):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor


    def rodar_game(self, leitor):
        if leitor == "com disco":
            print("Rodar midia fisica")
        elif leitor == "sem disco":
            print("Rodar midia digital")



video_game = Console("Sony", "PS4", "Preto")
print(video_game.modelo)
video_game.rodar_game("com disco")

video_game2 = Console("Sony", "PS5", "Branco")
print(video_game2.modelo)
video_game.rodar_game("com disco")

video_game3 = Console("Microsoft", "Series S", "Branco")
print(video_game3.modelo)
video_game.rodar_game("sem disco")

video_game4= Console("Microsoft", "Series X", "Preto")
print(video_game4.modelo)
video_game.rodar_game("com disco")
