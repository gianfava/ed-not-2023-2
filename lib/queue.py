class Queue:
    """
        ESTRUTURA DE DADOS FILA
        É uma estrutura de dados linear em que a operação
        de inserção ocorre no final da estrutura,
        enquanto a operacao d eremocao ocorre no inicio. Como consequencia,
        o funcionamento da fila pode ser descrito pelo proincipio FIFO
        o primeiro a entrar é o primeiro a sair
    """
    def __init__(self):
        """ Método Construtor"""
        self.__data = []    #ListaVazia

    def enqueue(self,val):
        """ 
            Método de Inserção
            Em filas, tem nome padronizado:enqueue
        """
        return self.__data.append(val)
    
    def is_empty(self):
        """ 
            Método que retorna se a fila está vazia ou não
        """
        return len(self.__data) == 0
    
    def dequeue(self):
        """ 
            Método de Remoção
            Em filas, tem nome padronizado:dequeue
        """
        if self.is_empty():
            raise Exception("ERRO: não é possível remover de uma fila vazia")
            #Remove do inicio (posicao 0)
        return self.__data.pop(0)

    def peek(self):
        """ 
            Método para consultar o primeiro item da fila,
            sem removê-lo
        """
        if  self.is_empty():
            raise Exception("ERRO: não é possível consultar de uma fila vazia")
            #Retorna o primeiro elemento (posicao 0)
        return self.__data[0]
    
    def __str__(self):
        """ 
            Método que retorna uma representação 
            da fila como string
        """
        return str(self.__data)