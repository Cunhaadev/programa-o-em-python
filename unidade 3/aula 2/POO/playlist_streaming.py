class Musica:
    def __init__(self, titulo:str, artista:str):
        self.titulo = titulo
        self.artista = artista
        self.views = 0
    def play(self):
        print(f"A música {self.titulo} está tocando!")
        self.views += 1
        print(self.views)
musica1 = Musica("333", "Matuê")
musica2 = Musica("9", "Drake")


while True:
    musica1.play()
    input()