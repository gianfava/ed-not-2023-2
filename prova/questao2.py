"""
    1) Identifique o algoritmo abaixo.
    Este é o algoritmo é o de Busca Binária

    2) Registre em comentário o propósito de cada uma das variáveis (de a a f).
    Comentado no código

    3) Há um erro no algoritmo. Identifique-o, descreva-o e corrija-o.
"""    

def a(b, c): # a = nome da função que equivale a busca binária, b = parametro lista de dados, c = valor a ser localizado nesta lista
    d = 0    # d = inicio da lista
    e = len(b) - 1  # e = fim da lista
    while d <= e: # enquanto o inicio da lista for menor ou igual ao fim faça...
        f = (d + e) // 2   # f = meio da lista
        #if c == b[f]: e = f # <<<< erro
        if c == b[f]: # CORREÇÃO verifica se o valor q está no meio da lista é = ao valor de busca...
            return f  # CORREÇÃO ... que retornará o valor do MEIO (f)
        elif c < b[f]: # se o valor for menor do q o valor do meio, reinicia a busca na metade esquerda da lista
            e = f - 1
        else: # se o valor for maior que o  valor do meio, reinicia a busca na metade direita da lista     
            d = f + 1
    return -1 #neste ponto, o valor de busca não existe na lista (b)

############

nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 47]
print(nums)
print(a(nums, 11))

# testado e localizada a posição 4, que é a posição do valor '11'