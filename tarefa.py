from atividade import Atividade


class Tarefa(Atividade):
    #Construtor da classe
    def __init__(self, titulo, descricao):

        self.__titulo = titulo
        self.__descricao = descricao

    # Getter -> Título
    def getTitulo(self):
        return self.__titulo

    # Getter -> Descrição
    def getDescricao(self):
        return self.__descricao

    # Setter -> Título
    def setTitulo(self, novoTitulo):
        self.__titulo = novoTitulo
        return

    # Setter -> Descrição
    def setDescricao(self, novaDescricao):
        self.__descricao = novaDescricao
        return
