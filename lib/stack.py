class Stack:
    """"
        ESTRUTURA DE DADOS DE PILHA
        Trata-se de uma estruturda de dados linear de acesso
        restrito, na qual tanto a operação de inserção (push), 
        quanto a operacao de remoção (pop) acontecem no final (topo)
        da estrutura. Como consequencia, o funcionamento da pilha
        obedece ao principio LIFO (Last In, First Out): o último 
        elemento a entrar é o primeiro a sair
    """

    def __init__(self):
        """ Método construtor """
        # Cria uma lista privada e vazia para armazenar os dados da pilha
        self.__data = []

    def push(self, val):
        """
            Método de inserção
            Em pilhas, tem nome padronizado: push
        """
        self.__data.append(val) # Insere no final
    def is_empty(self):
        """
            Método que verifica se a pilha está vazia ou não
        """
        return len(self.__data) == 0

    def pop(self):
        """
            Método para remoção
            Em pilhas, tem nome padronizado: pop
        """
        if self.is_empty():
            raise Exception("ERRO: impossível remover de uma pilha vazia")
        return self.__data.pop()

    def peek(self):
        """
            Método que permite consultar o valor no topo da pilha, sem remove-lo
            Em pilhas, tem nome padronizado: peek (espiadinha)
        """
        if self.is_empty():
            raise Exception("ERRO: impossível consultar uma pilha vazia")
        return self.__data[-1] #último elemento da lista
    
    def __str__(self):
        """
            Método que permite imprimir a lista interna como string
        """
        return str(self.__data)

