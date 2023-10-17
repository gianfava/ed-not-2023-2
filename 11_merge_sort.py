<<<<<<< HEAD
#divs -> numero de divisoes
#juncs -> numero de juncoes
#comps->  numero de comparacoes

=======
# Variáveis de estatística
# divs ~> número de divisões
# juncs ~> número de junções
# comps ~> número de comparações
>>>>>>> bf396c8511a31d8f384ba0f6596bc7756ab7d6ae
divs = juncs = comps = 0

def merge_sort(lista):
    """
        ALGORITMO DE ORDENAÇÃO MERGE SORT

        No processo de ordenação, esse algoritmo "desmonta"
        a lista original, contendo N elementos, até obter
        N listas com apenas um elemento cada uma. Em seguida,
<<<<<<< HEAD
        usado a técnica de mesclagem (merging), "remonta" a
        lista, desta vez com os elementos já em ordem.
    """
    global divs , juncs , comps 
    
=======
        usando a técnica de mesclagem (merging), "remonta" a
        lista, desta vez com os elementos já em ordem.
    """
    global divs, juncs, comps

>>>>>>> bf396c8511a31d8f384ba0f6596bc7756ab7d6ae
    # PARTE 1: DIVISÃO DA LISTA ORIGINAL EM LISTAS MENORES

    # Para que possa haver divisão da lista, esta deve ter
    # mais de um elemento
    if len(lista) > 1:

        # Encontra a posição do meio da lista, para fazer a divisão
        # em duas metades
        meio = len(lista) // 2
<<<<<<< HEAD
        
=======

>>>>>>> bf396c8511a31d8f384ba0f6596bc7756ab7d6ae
        # Tira uma cópia da primeira metade da lista
        sublista_esq = lista[:meio]
        # Tira uma cópia da segunda metade da lista
        sublista_dir = lista[meio:]

        divs += 1

        # Chamamos recursivamente a própria função para que ela
        # continue repartindo cada sublista em duas partes menores
        sublista_esq = merge_sort(sublista_esq)
        sublista_dir = merge_sort(sublista_dir)

        # PARTE 2: REMONTAGEM DA LISTA, ORDENADAMENTE

        pos_esq = pos_dir = 0
        ordenada = []       # Lista vazia

        # Compara os elementos das sublistas entre si e insere
        # na lista ordenada o menor dentre dois elementos
        while pos_esq < len(sublista_esq) and pos_dir < len(sublista_dir):
            
            comps += 1
            # O menor elemento está na sublista da esquerda
            if sublista_esq[pos_esq] < sublista_dir[pos_dir]:
                # "Desce" o elemento da esquerda para a lista ordenada
                ordenada.append(sublista_esq[pos_esq])
                pos_esq += 1        # Incrementa a posição da esquerda

            # O menor elemento está na sublista da direita
            else:
                # "Desce" o elemento da direita para a lista ordenada
                ordenada.append(sublista_dir[pos_dir])
                pos_dir += 1        # Incrementa a posição da direita

        # Verificação da sobra
        sobra = []

        # Sobra à esquerda
        if(pos_esq < pos_dir): sobra = sublista_esq[pos_esq:]
        # Sobra à direita
        else: sobra = sublista_dir[pos_dir:]

        juncs += 1

        # O resultado final é a junção (concatenação) da lista
        # ordenada com a sobra
        return ordenada + sobra
    
    else:
        return lista


########################################################

<<<<<<< HEAD
nums = [7, 5, 9, 0, 3, 4, 8, 1, 6, 2]

divs = juncs = comps = 0
nums_ord = merge_sort(nums)

print(f"Lista original: {nums} ")
print(f"Lista original: {nums_ord} ")
print(f"Divisões: {divs}, Junções: {juncs}, Comparações: {comps} ")

=======
# nums = [7, 5, 9, 0, 3, 4, 8, 1, 6, 2]
nums = [2, 8, 0, 7, 1, 9, 3, 6, 5, 4]

divs = juncs = comps = 0
nums_ord = merge_sort(nums)
print(f"Lista original: {nums}")
print(f"Lista ordenada: {nums_ord}")
print(f"Divisões: {divs}, junções: {juncs}, comparações: {comps}")
>>>>>>> bf396c8511a31d8f384ba0f6596bc7756ab7d6ae

###################################################################
# TESTE COM O ARQUIVO DE 1M+ NOMES

<<<<<<< HEAD
import sys
=======
import sys, tracemalloc
>>>>>>> bf396c8511a31d8f384ba0f6596bc7756ab7d6ae
sys.dont_write_bytecode = True    # Impede a criação do cache

# Importando a lista de nomes
from data.nomes_desord import nomes
from time import time

divs = juncs = comps = 0
<<<<<<< HEAD
hora_ini = time()
nomes_ord = merge_sort(nomes)
hora_fim = time()
print(nomes_ord)     # Lista após ordenação
print(f"Tempo gasto: {(hora_fim - hora_ini) * 1000}ms\n")
print(f"Divisões: {divs}, Junções: {juncs}, Comparações: {comps} ")
=======

tracemalloc.start()     # Inicia a medição do consumo de memória
hora_ini = time()
nomes_ord = merge_sort(nomes)
hora_fim = time()

# Captura as informações do gasto de memória
mem_atual, mem_pico = tracemalloc.get_traced_memory()
tracemalloc.stop()      # Termina a medição do consumo de memória

print(nomes_ord)     # Lista após ordenação
print(f"Tempo gasto: {(hora_fim - hora_ini) * 1000}ms\n")
print(f"Divisões: {divs}, junções: {juncs}, comparações: {comps}")
print(f"Pico de memória: { mem_pico / 1024 / 1024 } MB")
>>>>>>> bf396c8511a31d8f384ba0f6596bc7756ab7d6ae
