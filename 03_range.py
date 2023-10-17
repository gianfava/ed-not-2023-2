# range() é uma função que gera uma faixa de números.
# é muito usada em associações de listsa

#1) range() com 1 parâmetro: gera uma faixa que vai de 
# 0 (zero) até o valor do parâmetro -1
for num in range(10):
    print(num)

print("-" * 40)

#2) range() com 2 parâmetros: gera uma sequencia começando
# pelo valor do primeiro (inclusive) e ndo até
# o valor do segundo parâmetro (exclusive, NÃO ENTRA)
for i in range(10,15):
    print(i)

print("-" * 40)

# 3) range() com 3 parâmetros
#   1° limite inferior (inclusive)
#   2° limite superior (exclusive, NÃO ENTRA)
#   3° passo ( de quanto em quanto a sequência vai saltar; PODE SER NEGATIVO)
for i in range(1,22,3): # De 1 a 21 saltando de 3 em 3
    print(i)

print("-" * 40)

# range() com passo negativo
for i in range(10, 0, -1): #contagem regressiva de 10 a 1 
    print(i)

print("-" * 40)
