class Graph:
    """
        Estrutura de Dados Grafo
        É uma estrutura de dados não linera formada por vertices
        (nodos) e arestas. Sua principal finalidade é representar
        as relações entre diferentes entidades. tais relações podem ser
        bidirecionais , resultando em grafos não direcionados, ou
        unidirecionais (digrafos). Entre suas aplicações estão
        representações de redes de computadores, mapas, caminhos e redes sociais.
    
    """
    def __init__(self, is_directed = False):
        """ Método Construtor"""
        self.__is_directed = is_directed    # o grafo é direcionado?
        
        #__data__ aramazenará o grafo no formato LISTA DE ADJACENCIA
        self.__data = {}    # Dicionário Vazio
        print("Grafo: ", self.__data)
    
    def add_vertex(self,val):   # vertice
        """
            Método que adiciona um vértice ao grafo
        """
        # Verifica se o vértice já existe no dicionário.
        # A criação só ocorre se o vertice ainda não existir
        if not val in self.__data:
            self.__data[val]  = set()    # Conjunto vazio
        print("Grafo: ", self.__data)
    
    def add_edge(self, origin, dest, label = None):
        """
            Método que adiciona uma aresta entre dois vértices
            origin: vértice de origem
            dest: vértice de destino
            label: rótulo descritivo do relacionamento (opcional)
        """
        # Cria os vertices de origem e destino, caso ainda não existeam
        if not origin in self.__data: self.add_vertex(origin)
        if not dest in self.__data: self.add_vertex(dest)

        # Monta a aresta
        edge1 = (dest, label)   # isto é uma tupla("lista imutável")

        # Adiciona a aresta origem -> destino
        self.__data[origin].add(edge1)

        # Se o grafo não for direcionado, devemos adicionar também
        # uma aresta no sentido oposto, isto é, destino -> origem
        if not self.__is_directed:
            edge2 = (origin, label) #tupla
            self.__data[dest].add(edge2)
        print("Grafo: ", self.__data)
        