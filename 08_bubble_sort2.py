comps = trocas = passd = 0

def bubble_sort(lista):
    """
<<<<<<< HEAD
    ALGOTITMO DE ORDENAÇÃO BUBBLE SORT
    Percorre a lista a ser ordenada em sucessivas passadas,
    trocando entre si dois elemntos adjacentes sempre que
    o segundo for MENOR que o primeiro. Efetua tantas
    passadas quanto necessárias, até que, na última delas,
    nenhuma toca tenha sido realizada

    versao modificada 1ue diminui o tempo de comparacao

    """
=======
      ALGORITMO DE ORDENAÇÃO BUBBLE SORT
      Percorre a lista a ser ordenada em sucessivas passadas,
      trocando entre si dois elementos adjacentes sempre que
      o segundo for MENOR que o primeiro. Efetua tantas
      passadas quanto necessárias, até que, na última delas,
      nenhuma troca tenha sido realizada

      ESTA VERSÃO TEM UMA PEQUENA OTIMIZAÇÃO QUE VAI DIMINUINDO
      A QUANTIDADE DE COMPARAÇÕES A CADA PASSADA
    """

>>>>>>> bf396c8511a31d8f384ba0f6596bc7756ab7d6ae
    # Usando as variáveis globais
    global comps, trocas, passd
    comps = trocas = passd = 0

<<<<<<< HEAD
    #Loop eterno, não sabemos de antemao quantas passadas
    #serã necessárias
    while True:
        # inicio de uma nova passada
        passd += 1

        #Controla se houve trocas na passada
        trocou = False

        #Percurso da Lista, do primeiro ao penultimo elemento,
        #com acesso a cada posição, Na primeira passada
        # nas demais o percurso vai diminuindo uma posição
        for pos in range(len(lista) - passd):

            #se o valor que está a frente na lista (pos + 1)
            #for menor que aquele que esta atras (pós)
            #faz uma TROCA
            if lista[pos+1]<lista[pos]:
                lista[pos+1], lista[pos] = lista[pos], lista[pos+1]
                trocou = True # Houve troca na passada
                trocas +=1

            # O if representa uma comparacao
            comps +=1    

        if not trocou:  # Não houve troca na passada
            break       # Interrompe o loop eterno

##############################################################################

nums = [7, 5, 9, 0, 3, 4, 8, 1, 6, 2]
# nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]  # melhor caso
# nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]    # pior caso

print("ANTES: ", nums)
bubble_sort(nums)
print("DEPOIS: ", nums)
print(f"Comparações: {comps}, trocas: {trocas}, passadas: {passd}")

##############################################################################
#fazendo a busca em um arquivo com 1 M+ nomes
# #Importando a lista de nomes

# import sys
# sys.dont_write_bytecode = True #Impede a criação d cache

# from data.nomes_desord import nomes
# from time import time

# nomes1000 = nomes[:10000]

# hora_ini= time()
# pos1 = bubble_sort(nomes1000)
# hora_fim = time()
# print(nomes1000)
# print(f"Tempo Gasto: {(hora_fim-hora_ini) * 1000}ms\n")



=======
    # Loop eterno, não sabemos de antemão quantas passadas
    # serão necessárias
    while True:

        # Início de uma nova passada
        passd += 1

        # Controla se houve trocas na passada
        trocou = False

        # Percurso da lista, do primeiro ao PENÚLTIMO elemento,
        # com acesso a cada posição, NA PRIMEIRA PASSADA
        # Nas demais passadas, o percuso vai diminuindo uma posição
        for pos in range(len(lista) - passd):
            
            # Se o valor que está à frente na lista (pos + 1)
            # for MENOR do que aquele que está atrás (pos),
            # faz uma TROCA
            if lista[pos + 1] < lista[pos]:
                lista[pos + 1], lista[pos] = lista[pos], lista[pos + 1]
                trocou = True   # Houve troca na passada
                trocas += 1

            # O if representa uma comparação
            comps += 1

        if not trocou:      # Não houve troca na passada
            break           # Interrompe o loop eterno

############################################################

nums = [7, 5, 9, 0, 3, 4, 8, 1, 6, 2]

# Melhor caso
# nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Pior caso
# nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

print("ANTES:", nums)
bubble_sort(nums)
print("DEPOIS:", nums)
print(f"Comparações: {comps}, trocas: {trocas}, passadas: {passd}")

###################################################################
# TESTE COM O ARQUIVO DE 1M+ NOMES

# import sys
# sys.dont_write_bytecode = True    # Impede a criação do cache

# # Importando a lista de nomes
# from data.nomes_desord import nomes
# from time import time

# nomes100000 = nomes[:100000]

# hora_ini = time()
# bubble_sort(nomes100000)
# hora_fim = time()
# print(nomes100000)     # Lista após ordenação
# print(f"Tempo gasto: {(hora_fim - hora_ini) * 1000}ms\n")
>>>>>>> bf396c8511a31d8f384ba0f6596bc7756ab7d6ae
