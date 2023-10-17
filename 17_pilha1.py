from lib.stack import Stack

# Criando uma nova pilha
pilha = Stack()

palavra  = 'LARANJA'

#  empilhando as letras da palavra
for letra in palavra:
    pilha.push(letra)
    print(pilha)

print('-' * 70)

inverso = ""

# Desempilhando e colocando cada letra retirada
# dentro da string inverso

while not pilha.is_empty():
    print(pilha)
    inverso += pilha.pop()


print('-' * 70)

print(f"Palavra original: {palavra}")
print(f"Palavra invertida: {inverso}")