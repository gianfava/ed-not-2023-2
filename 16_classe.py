"""
    Classe é uma estrutura que representa conjuntamente
    dados e algoritmos. Uma classe pode ser comparada a
    uma "assadeira", com a qual se pode produzir diferentes
    tipos de "assados" (objetos), variando os "ingredientes"
    (dados) e o "modo de fazer" (algoritmos). Apesar dessa
    variação, todos os objetos criados a partir de uma mesma
    classe terão sempre o formato determinado por esta.
"""
from math import pi

class FormaGeometrica:
    """
        Por convenção nomes de classe seguem o formato PascalCase
        (primeira letra de cada palavra em maiúscula).

        Uma classe pode ter, dentro de si, tanto dados quanto funções
        (estas, representando os algoritmos). Uma função especial,
        chamada __init__, é chamada sempre que se tenta criar um novo
        objeto a partir de uma classe. Essa função especial é chamada
        CONSTRUTOR.

        No contexto de classes e de programação orientada a objetos:
        ~> funções passam a ser chamadas MÉTODOS, seu primeiro
           parâmetro é sempre self, que representa o próprio objeto
        ~> variáveis passam a ser chamadas ATRIBUTOS
    """

    def __init__(self, base, altura, tipo):
        """ Método construtor """

        # Validação do valor da base
        # Deve ser numérico e maior do que zero
        if type(base) in [int, float] and base > 0:
            # Guarda o valor passado dentro da classe
            self.__base = base
        else:
            # Gera um erro que impede a criação do objeto
            raise Exception(f"ERRO: o valor da base ({base}) deve ser numérico e maior do que zero.")
        
        # Validação do valor da altura
        # Deve ser numérico e maior do que zero
        if type(altura) in [int, float] and altura > 0:
            # Guarda o valor passado dentro da classe
            self.__altura = altura
        else:
            # Gera uma exceção que impede a criação do objeto
            raise Exception(f"ERRO: o valor da altura ({altura}) deve ser numérico e maior do que zero.")
        
        # Validação do valor do tipo
        # Deve aceitar apenas uma das três letras: R, T ou E
        if tipo in ["R", "T", "E"]:
            # Guarda o valor passado dentro da classe
            self.__tipo = tipo
        else:
            # Gera uma exceção que impede a criação do objeto
            raise Exception(f"ERRO: o valor do tipo ({tipo}) deve ser R, T ou E.") 
        
    def set_base(self, base):
        '''funcao setter para oa tributo self.__base'''
        if type(base) in [int, float] and base > 0:
            self.__base = base
        else:
            raise Exception(f"ERRO: o valor da base({base}) de veser numerico e maior q 0")
    
    
    def set_altura(self, altura):
        '''funcao setter para oa tributo self.__base'''
        if type(altura) in [int, float] and altura > 0:
            self.__altura = altura
        else:
            raise Exception(f"ERRO: o valor da altura({altura}) deveser numerico e maior q 0")

    def set_tipo(self, tipo):
        '''funcao setter para oa tributo self.__tipo'''
        if type(tipo) in [int, float] and tipo > 0:
            self.__base = tipo
        else:
            raise Exception(f"ERRO: o valor da tipo({tipo}) de veser numerico e maior q 0")


   
    def __str__(self):

        """ 
            Gera uma representação dos valores armazenados dentro
            do objeto como string, para podermos visualizá-los
        """
        return f"< [OBJETO] base: {self.__base}; altura: {self.__altura}; tipo: {self.__tipo} >"
    
##################################################################

# Triângulo de 10x30
triangulo1 = FormaGeometrica(10, 30, "T")
print("triangulo1", triangulo1)

# Elipse de 60x90
elipse1 = FormaGeometrica(60, 90, "E")
print("elipse1", elipse1)

# Retângulo de 7,5x22,5
retangulo1 = FormaGeometrica(7.5, 22.5, "R")
print("retangulo1", retangulo1)

#tentativa de criação de forma com dados errados
forma1= FormaGeometrica(5, 5.8, "R")
print("forma1", forma1)

print("-" *78)

triangulo1.base = -12
triangulo1.altura = "tomate"
triangulo1.tipo = False
print("Objeto triangulo1 modificado ", triangulo1)