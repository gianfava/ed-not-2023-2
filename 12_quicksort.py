# variaveis de estatistica
comps = trocas = passd = 0

def quick_sort(lista, ini=0, fim=None):
    """
        ALGORITMO DE ORDENAÇÃO QUICK SORT
        Escolhe um dos elementos da lista para ser o pivô (na nossa 
        implementação , será o ultimo elemento) e, na primeira 
        passada, divide a lista a partir da posição final do pivo,
         em uma sublista a esquerda , contendo apenas valores menores
         que o pivo, e outra sublista a direita, que contem apenas
         valores maiores que o pivo.
         Em seguida, recursivamente, repete o processo em cada uma das
         sublistas, até que toda a lista esteja ordenada.
    """

    # Quando não soubermos o valor da variavel "fim", atribuimos a
    # ela o valor da ultima posicao da lista
    if fim is None: fim = len(lista) -1

    # print(f"ini = {ini}, fim = {fim}")

    # Para que o algoritmo trabalhe, é necessário que a faixa delimitada
    # pelas variaveis "ini" e "fim" tenha pelo menos dois elementos
    # Caso contrario, saimos da função sem fazer nada
    if fim <=ini:return


    global comps, trocas, passd
    #Inicialização das Variaveis
    pivot = fim
    div = ini -1

    passd += 1

    #Percorre a lista da posição "ini" ate a posicao "fim -1"
    for pos in range(ini,fim):
        # Se o elemnto da posição "pos" for MENOR q o elemento da 
        # da posição pivot , executa algumas acaoes
        comps += 1

        if lista[pos]< lista[pivot]:
            div +=1 # Chega o div um apocição para fronte

            # Efetua a troca entre os elemntos das posições pos e div
            # desde que essas variavels tenha valor distinto entre si
            comps += 1
            if pos != div and lista[pos] < lista[div]:
                lista[pos], lista[div] =  lista [div], lista[pos]
                trocas += 1

    # Depois que pos chega em sua posicao final div deve ser incrementado uma ultima vez
    div +=1

    # caso os valores das posicoes pivot e div sejam diferentes entre ...si , efetua a troca mutua dos elemntos dessas posicoes, caso o  ....primeiro seja menor que o segundo
    comps += 1
    if pivot != div and lista[pivot] < lista[div]:
        lista[pivot], lista[div] = lista[div], lista[pivot]
        trocas += 1

    #neeste ponto o elemneto da posi

    # Chamamos recursivamente a function para ordenar a sublista a esquerda da posicao div
    quick_sort(lista, ini, div-1)

    # a mesma coisa só que para a sublista a direita de div
    quick_sort(lista, div +1, fim)

#############################################

nums = [7, 5, 9, 0, 3, 4, 8, 1, 6, 2]

comps = trocas = passd = 0
quick_sort(nums)
print(nums)
print(f"Comparações: {comps}, trocas: {trocas}, passadas: {passd}")

##################################################################
# # TESTE COM O ARQUIVO DE 1M+ NOMES

# import sys
# sys.dont_write_bytecode = True    # Impede a criação do cache

# # Importando a lista de nomes
# from data.nomes_desord import nomes
# from time import time

# # nomes = nomes[:10000]

# hora_ini = time()
# quick_sort(nomes)
# hora_fim = time()
# print(nomes)     # Lista após ordenação
# print(f"Tempo gasto: {(hora_fim - hora_ini) * 1000}ms\n")
# print(f"Comparações: {comps}, trocas: {trocas}, passadas: {passd}")