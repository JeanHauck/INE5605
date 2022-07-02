from enum import Enum
class IncidenciaImposto(Enum):
    PRODUCAO = 1,
    SERVICOS = 2,
    VENDAS = 3,
    TODOS = 4

class Imposto():
    def __init__(self, aliquota: float, incidencia_imposto: IncidenciaImposto):
        self.__aliquota = aliquota
        self.__incidencia_imposto = incidencia_imposto

    @property
    def aliquota(self):
        return self.__aliquota

    @property
    def incidencia_imposto(self):
        return self.__incidencia_imposto

imposto = Imposto(10.0, IncidenciaImposto.PRODUCAO)

if imposto.incidencia_imposto == IncidenciaImposto.PRODUCAO:
  print("ACHOU!")
