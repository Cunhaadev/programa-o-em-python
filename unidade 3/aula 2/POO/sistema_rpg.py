class Personagem:
    def __init__(self, nome):
        self.nome = nome
        self.nivel = 1
        self.experiencia = 0
    def ganharxp(self, xp):
        self.experiencia += xp
        if self.experiencia > 100:
            self.nivel =+ 1
            self.experiencia = 0