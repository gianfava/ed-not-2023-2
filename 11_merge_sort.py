def merge_sort(lista):
    """
        ALGORITMO DE ORDENAÇÃO MERGE SORT
        No processo de ordenação, esse algoritmo "desmosta"
        a lista original, contendo N elementos, até obter
        N listas com apenas um elemento cada uma. Em seguida,
        usado a técnica de mesclagem (merging), "remonta a lsta,
        desta vez com os elemntos já em ordem.
    """
    # PARTE 1: Divisão da Lista Original em Listas Menores

    #Para que possa haver divisao da lista, esta deve ter
    #mais de um elemento
    if len(lista)> 1: 

        # Encontra a posição do meio da lista para fazer a divisao
        # em duas metades
        meio = len(lista) // 2

        # Tira uma cópia da primeira metade da lista
        sublista_esq = lista[:meio] # do começo até o meio
         # Tira uma cópia da segunda metade da lista
        sublista_dir = lista[meio]:# do meio até o final

        # Chamamos recursivamente a própiria função para que ela
        #continue repartindo cada sublista em duas partes menores
        sublista_esq = merge_sort(sublista_esq)
        sublista_dir = merge_sort(sublista_dir)

        #PARTE 2  = Remontagem da Lista Ordenadamente

        pos_esq= pos_dir = 0
        ordenada = []   #Lista vazia

        #Compara os elemetos das sublistas entre si e insere
        # na lista ordenadao menor dentre dis elemntos
        while pos_esq<len(sublista_esq) and pos_dir<len(sublista_dir):
            if sublista_esq[pos_esq] < sublista_esq[pos_esq]
            pos_es +=1
            else:
                ordenada.append(sublista_dir[pos_dir])
                pos_dir +=1
        sobra =  []

        if(pos-esq < pos_dir): sobra = sublista_esq[pos_esq:]

        else:sora = sublista_dir[pos_dir:]

        return ordenada + sobra