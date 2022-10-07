from datetime import datetime
from atividade import Atividade


# Classe -> Evento
class Evento(Atividade):

    #Construtor da classe
    def __init__(self,
                 titulo: str,
                 descricao: str,
                 local: str,
                 data: datetime = None):

        self.__titulo = titulo
        self.__descricao = descricao
        self.__local = local
        self.__data = data

    # Getter -> Título
    def getTitulo(self):
        return self.__titulo

    # Getter -> Descrição
    def getDescricao(self):
        return self.__descricao

    # Getter -> Local
    def getLocal(self):
        return self.__local

    # Getter -> Data
    def getData(self):
        return self.__data

    # Setter -> Título
    def setTitulo(self, novoTitulo):
        self.__titulo = novoTitulo
        return

    # Setter -> Descrição
    def setDescricao(self, novaDescricao):
        self.__descricao = novaDescricao
        return

    # Setter -> Local
    def setLocal(self, novoLocal):
        self.__local = novoLocal
        return

    # Setter -> Data
    def setData(self, novaData):
        self.__data = novaData
        return
