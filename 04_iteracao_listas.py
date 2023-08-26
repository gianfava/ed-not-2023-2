#Listas de Frutas

frutas = [" 1 -laranja", " 2 -maçã", " 3 -uva", " 4 -pêra", " 5 -mamão", " 6 -abacate", " 7 -amora"]

#Para percorrer uma lista e exibir apenas seus elementos.
#usamos a estrutura for...in
for f in frutas:
    print(f)

print("-" * 40)

#Imprimindo uma lista de trás para frente: reversed()
for x in reversed(frutas):
    print(x)

print("-" * 40)

# No entanto, precisamos exibir além do valor do elemento, sua posição
for pos in range(len(frutas)):
    print(frutas[pos], ":", pos)

print("-" * 40)

for pos in range(len(frutas)):
    # print((frutas[pos])* pos)
    # print("A fruta", frutas[pos], " está na posição ", pos, ".")
    print(f"A fruta {frutas[pos]} está na posição {pos}.")

print("-" * 40)

# for pos in range(20): #piramide
#     print(("*") * pos)

print("-" * 40)

# #As vezes é necessário percorrer a lista d etrás para frente
# mas tendo tb acesso a posição dos elementos, para isso
# usamos a estrutura for..in , range() com três parâmetros e len()

for i in range (len(frutas)-1, -1, -1): # onde (len(frutas)-1 é a posição inicial, -1 é a posição final, -1 é o passo)
    print(f"a fruta {frutas[i]} está na posição {i} .")

