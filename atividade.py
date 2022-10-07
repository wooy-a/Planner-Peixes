# Classe -> Atividade
class Atividade():
    #Construtor da classe
    def __init__(self, 
                    titulo: str, 
                    descricao: str):
      
        self.__titulo = titulo
        self.__descricao = descricao

    # Getter -> Titulo
    def getTitulo(self):
        return self.__titulo
    
    # Getter -> Descrição
    def getDescricao(self):
        return self.__descricao

    # Setter -> Titulo
    def setTitulo(self, novoTitulo):
        self.__titulo = novoTitulo
        return
    
    # Setter -> Descrição
    def setDescricao(self, novaDescricao):
        self.__descricao = novaDescricao
        return