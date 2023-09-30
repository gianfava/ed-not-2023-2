"""
    1) Identifique o algoritmo abaixo.
    Este é o algoritmo Selection Sort.

    2) Registre em comentário o propósito de cada uma das variáveis (de v a z).
    Comentários registrados no código.

    3) Há um erro no algoritmo. Identifique-o, descreva-o e corrija-o.
    Sim, o erro foi ao comparar com a posição x do primeiro for, sendo que o correto era comparar posição z (a subsequente) 
"""

def z(y): # z é o nome da função e y o parametro a ser passado
    for x in range(len(y) - 1):# iterador x que vai da primeira até a penultima posição
        w = x + 1 #inicia supondo que a posição do menor valor da lista é a subsequente à posição selecionada
        for v in range(x + 2, len(y)):#percorre a lista mais uma vez, de 2 em 2 posições até a última
            #if y[v] < y[x]: # se o valor encontrado na posição v for MENOR do que o valor da posição x (erro) o certo seria w, então...
            if y[v] < y[w]:# <<<correção
                w = v #... w atualiza para a posição v
        if y[w] < y[x]: # se o primeiro for MENOR que o segundo, acontece a troca entre eles
            y[x], y[w] = y[w], y[x]

# z nome da função =  selection sort
# y lista/parametro
# x pos_sel = iterador posicao selecionada
# w pos_menor = posição menor
# v pos  =  iterador posicao
nums = nums = [9, 0, 1, 2, 3, 4, 5, 6, 7, 8]

print("ANTES:", nums)
z(nums)
print("DEPOIS:", nums)

#testado! ordenação selection sort retornou os numeros na ordem correta
