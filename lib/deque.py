class Deque:

    def __init__(self):
        #metodo construtor
        self.__data = []    # lista vazia
    
    def insert_front(self, val):
        #inserçaõ no inicio (posição 0)
        self.__data.insert(0,val)
    
    def insert_back(self,val):
        #insertion no final
        self.__data.append(val)
    
    def is_empty(self):
        return len(self.__data) == 0

    def remove_front(self):
        #remocao do final
        if self.is_empty():
            raise Exception("ERRO: impossível remover de um deque vazio")
            #remove da posicao 0
        return self.__data.pop(0)
    
    def remove_back(self):
        #remocao do final
        if self.is_empty():
            raise Exception("ERRO: impossível remover de um deque vazio")
            #remove da ultima posicao 
        return self.__data.pop()
    
    def peek(self, front = True):
        #consulta de um elemento do deque
        #se o parametro front for True ou tiver sido
        #omitido retorna o primeiro elemento.
        # Senao retorna o ultimo
        if front:
            return self.__data[0]   #primeiro elemento
        else:
            return self.__data[-1]    #ultimo elemento
    
    def __str__(self):
        #retorna uma representacao do deque como string
        return str(self.__data)

