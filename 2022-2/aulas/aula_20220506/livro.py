from br.ufsc.exemplo.genero import Genero

class Livro:
    def __init__(self, titulo, genero: Genero):
        self.titulo = titulo
        self.genero = genero

