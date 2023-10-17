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

#SUBSTITUINDO VALORES EXISTENTES 

print("ANTES:", legumes)
#Substituindo o valor da posição 3
legumes[3] = "vagem"

legumes[0] = "mandioca"

legumes[-1] = "milho"

print("DEPOIS:", legumes)

print("-" * 40) # traço de 40 hifens

#6) DETERMINANDO A QUANTIDADE DE ELEMENTOS NA LISTA: len()
print("Número de elementos na lista de valores:", len(valores))
print("Número de elementos na lista de legumes:", len(legumes))

print("-" * 40) #Traço de 40 hifens

#7) REMOVENDO O ÚLTIMO ELEMENTO DE UMA LISTA: pop()

print("antes: ", valores)
removido = valores.pop()
print("valor removido: ", removido)
print("DEPOIS:", valores)

print("-" * 40) # traço de 40 hífens

#8)REMOVENDO UM ELEMENTO POR SUA POSIÇÃO: pop() com parâmetro
removido = valores.pop(3)  #Remove o elemento da posição 3
print("valor removido da posição 3:", removido)
print(valores)
removido = valores.pop(0)  #remove o elemento da primeira posição
print("valor removido da primeira posição:", removido)
print(valores)

print("-" * 40) 

#9) REMOVENDO UM ELEMENTO POR SEU VALOR: remove()
print("ANTES:", legumes)
legumes.remove("abobrinha")
print("APOS REMOÇÃO DE abobrinha:", legumes)

print("-" * 40) 

# acrescentando alguns legumes para aumentar a lista
legumes.append("beterraba")
legumes.append("abobrinha")
legumes.append("batata doce")
legumes.append("mandioquinha")
legumes.append("cará")
legumes.append("nabo")

#10) FATIANDO UMA LISTA
# fatiar sigifica copiar uma parte da lista (uma sublista) para uma nova lista

print(legumes)

# cria uma sublista que contém os elementos da posição 2 até a posição 7
# (posição 8 não entra)

sublista2_7 = legumes [2:8]
print("Sublista de 2 a 7: ", sublista2_7)

# cria uma sublista que contém os elementos do inicio até a posição 5
# (posição 6 NÃO ENTRA)
sublista0_5 = legumes[:6]
print("Sublista de 0 a 5:", sublista0_5)

# cria uma sublista que contem os elementos da posição 8 até o final
sublista8_fim = legumes[8:]
print("Sublista de 8 até o fim: ", sublista8_fim)

