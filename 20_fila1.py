from lib.queue import Queue

# Criando uma nova fila
fila = Queue()

#  Insere algumas pessoas na fila
fila.enqueue("Leotildes")
fila.enqueue("Orozimbo")
fila.enqueue("Waldisney")
fila.enqueue("Adamastor")

print(fila)

#Atende uma pessoa
atendido = fila.dequeue()
print(f"Atendido: {atendido}")
print(fila)

#Uma nova pessoa chegou a fila
fila.enqueue("Marcineia")
print(fila)

#Consultando quem será o próximo a ser
#atendido sem retira lo da fila
proximo = fila.peek()
print(f"Proximo: {proximo}")
print(fila)

