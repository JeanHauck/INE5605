# ======================================================================================================================
# 1. Relacionamento de COMPOSICAO
# ======================================================================================================================

# Definindo as classes:

# Classe Pagina

class Pagina:
    def __init__(self, texto, numero):
        self.__texto_da_pagina = texto
        self.__numero = numero

    @property
    def texto(self):
        print("Executou property")
        return self.__texto_da_pagina

    @texto.setter
    def texto(self, texto):
        print("Executou o setter")
        self.__texto_da_pagina = texto

# Classe Autor

class Autor:
    def __init__(self, nome):
        self.nome = nome

# Classe Livro

class Livro:

    def __init__(self, texto: str, numero: int, autor: Autor = None):
        self.__autor = autor
        primeira_pagina = Pagina(texto, numero)
        self.__paginas = []
        self.__paginas.append(primeira_pagina)

    def adiciona_pagina(self, texto, numero):
        pagina = Pagina(texto, numero)
        self.__paginas.append(pagina)

# Exercitando relacionamento de composicao

autor = Autor("Jean")

livro = Livro("Texto livro", 1, autor)
livro.adiciona_pagina("Texto de uma pagina do livro", 1)

livro_2 = Livro("Texto livro", 1)
livro_2.adiciona_pagina("Texto de outra pagina do livro", 1)


# ======================================================================================================================
# 2. Problemas na associacao bidirecional muitos para muitos
# ======================================================================================================================

# Classe Aluno ----------------
class Aluno:
    def __init__(self, matricula):
        self.matricula = matricula
        self.turmas = []

    def matricula_na_turma(self, turma):
        if (turma is not None) and (isinstance(turma, Turma)):
            if turma not in self.turmas:
                self.turmas.append(turma)
                turma.matricula_aluno(self)

# Classe Turma ----------------
class Turma:
    def __init__(self, codigo):
        self.codigo = codigo
        self.alunos = []

    def matricula_aluno(self, aluno):
        if (aluno is not None) and (isinstance(aluno, Aluno)):
            if aluno not in self.alunos:
                self.alunos.append(aluno)
                aluno.matricula_na_turma(self)

# Testando Relacoes Bidirecionais ----------------

aluno_1 = Aluno("Aluno 1")
aluno_2 = Aluno("Aluno 2")
aluno_3 = Aluno("Aluno 3")

turma_A = Turma("Turma A")
turma_B = Turma("Turma B")

aluno_1.matricula_na_turma(None)
aluno_1.matricula_na_turma(turma_A)
aluno_1.matricula_na_turma(turma_B)
aluno_2.matricula_na_turma(turma_B)
aluno_3.matricula_na_turma(turma_A)

turma_A.matricula_aluno(aluno_1)
turma_B.matricula_aluno(aluno_1)
turma_B.matricula_aluno(aluno_2)

print("-"*20)
print("Alunos da Turma A: ")
for aluno_na_turma in turma_A.alunos:
    print("Aluno: ", aluno_na_turma.matricula)

print("-"*20)
print("Turmas do Aluno 3: ")
for turma_do_aluno in aluno_3.turmas:
    print("Turma: ", turma_do_aluno.codigo)

