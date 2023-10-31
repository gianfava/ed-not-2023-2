from lib.deque import Deque

# Criando deque
deque = Deque()

#  Deque se comportando como fia comum algumas pessoas na fila
deque.insert_back("Antero")
deque.insert_back("Olentina")
deque.insert_back("Gaudencio")
deque.insert_back("Hildebrando")
deque.insert_back("Iranildes")

print(deque)

removido_frente = deque.remove_front()
print(f"Removido da Frente: {removido_frente}")
print(deque)

deque.insert_back("Tiburcio")
print(deque)

primeiro = deque.peek()
print(f"Primeiro da Fila: {primeiro}")
print(deque)


#Usando Recursos Exclusivos do DEQUE

#Insercao prioritaria
deque.insert_front("Emereciana")
print(deque)

#Desistencia da fila
desistente = deque.remove_back()
print(f"Desistente: {desistente}")
print(deque)

#Segunda Insercao prioritaria
deque.insert_front("Deusdete")
print(deque)

