class DoublyLinkedList:
    """
        ESTRUTURA DE DADOS LISTA DUPLAMENTE ENCADEADA
        Trata-se de uma lista linear em que seus elementos
        (chamados nodos ou nós) não estão fisicamente
        adjacentes uns aos outros, mas ligados logicamente 
        por ponteiros que indicam o nodo anterior e o nodo
        seguinte da sequencia. Não possui restrição de acesso -
        inserções, exclusões e consultas podem ser executadas
        em qualquer posição da lista
    """

    class Node:
        """
            Classe interna que representa a unidade de
            informação (nodo) armazenada pela lista
            duplamente encadeada
        """
        def __init__(self, data):
            """ Construtor da Classe interna Node"""
            self.prev = None    # ponteiro para o nodo anterior
            self.data = data    # dado útil para o usuário
            self.next = None    # ponteiro para o modo seguinte

    def __init__(self):
        """
            Constrtutor da classe principal DoublyLinkedList
        """
        self.__head = None  # Ponteiro para o primeiro nodo
        self.__tail = None  # Ponteiro para o último nodo
        self.__count = 0  # Quantidade de nodos da lista
    
    def get_count(self):
        """ Método que retorna a qde de nodos da lista"""
        return self.__count
    
    def insert(self, pos, val):
        """ Método que insere na posição "pos" o valor 'val' """
        #Criamos um novo nodo p/ armazenar val e tambem
        #os ponteiros 'prev' e 'next' , ambos apontando inicialmente para o None
        new = self.Node(val)

        # 1º caso: lista esta vazia, e 'new' será o primeiro e ultimo nodo ao msm tempo
        if self.get_count() == 0:   # Lista vazia
            self.__head = new
            self.__tail = new
        
        # 2º caso: insercao no inicio da lista (posição 0)
        elif pos == 0:
            new.next = self.__head
            self.__head.prev = new
            self.__head = new
        
        # 3º caso: insercao no final da lista
        # Obs: consideramos como posição final qq uma q
        # seja > = self.get_count()
        elif pos >= self.get_count():
            new.prev = self.__tail
            self.__tail.next = new
            self.__tail = new
       
        # Incrementa a contagem de nodos da lista
        self.__count += 1

