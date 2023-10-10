"""
    1) Identifique o algoritmo abaixo.
    Este é o algoritmo Bubble Sort.

    2) Registre em comentário o propósito de cada uma das variáveis (de a a d).
    Comentado no código

    3) Há um erro no algoritmo. Identifique-o, descreva-o e corrija-o.
    Sim, a lista b (parametro) precisa receber a posição em 'd' e não em 'c'

"""

def a(b):   # a = definição/nome da função , b= parâmetro/lista de dados
    while True: #loop eterno até fazer as passadas necessárias
        c = False   # c = controla se houve trocas na passada
        for d in range(len(b) - 1):# d = iterador ou posição para o loop do 'for'
            if b[d + 1] < b[d]: # se o valor q esta na frente da lista for menor do q esta atras, faz a troca
                #b[d + 1], b[c] = b[c], b[d + 1] <<< ERRO: a lista b precisa receber a posição em 'd' e não em 'c'
                b[d + 1], b[d] = b[d], b[d + 1]  # <<< correção 
                c = True     # troca na passada
        if not c:            # ñ houve troca na passada
            break            #interrompe o loop

######

nums = [7, 8, 3, 2, 1, 4 ,6, 0, 5, 9]
print('lista original: ', nums)
a(nums)
print('lista ordenada: ', nums)
 

#testado e funcionado.