# #Listas
# Listas são uma forma de armazenar mais d euma valor em uma única variável
# Os valores podem ser de tipos diferentes

# Uma lista de numeros
valores = [2,3,5,7,9,11]
legumes = ['batata', 'tomate', 'cenoura']

# Uma lista com valores de tipos variados
mix = ["batata", 1.25, True, "tomates", 44]

# Operações sobre Listas
# Percurso: significa percorrer a lista do primeiro ao ultimo elemento
#Imprimindo cada um dos elementos da lista, um por linha:

for val in valores:
    print("---->",val)

print("---------------")

for x in range(10):
    resultado = x * 8
    print(x, "x 8 = ", resultado)
    print("---------------")
    
    
# 2) Inserindo un novo elemento no FIM da lista com APPEND

print(valores)
print(legumes)

valores.append(13)
legumes.append("cebola")

print(valores)
print(legumes)

# 3) Inserindo un novo elemento em posição específica com INSERT
#      Parâmetros: 
#       1º a posição onde será inseridoo novo elemento
#       2º o novo elemento a ser inserido

legumes.insert(2,'mandioquinha')
print(legumes)
legumes.insert(0,'beterraba')
print(legumes)

# 4) Acessando valores em uma posição específica 

print("elemento na QUARTA posição", valores[3])
print("elemento na PRIMEIRA posição", valores[0])
print("elemento na ÚLTIMA posição", valores[-1])
print("elemento na PENULTIMA posição", valores[-2])