<<<<<<< HEAD
def calc_imc(peso, altura):
    return peso / altura ** 2

# p = 80
# a = 1.75
# imc = calc_imc(p,a)
# print (' O seu imc é: ',  round(imc,1))

# print (calc_imc(80,1.75))//  ocultei 


from math import pi

""" 
    # Função que Calcula Figura Geométrica Plana
"""

def calc_area (base, altura, tipo):

    if (tipo==1): # 1 = retangulo ou quadrado
        resultado = base * altura
        print("Area do retangulo = ", round(resultado,1))
    elif (tipo==2): # 2  =  triangulo
        resultado= (base * altura) / 2
        print("Area do Triangulo = ", round(resultado,1))
    elif (tipo==3): # 3  =  elipse
        resultado= (base/2) * (altura/2) * pi 
        print("Area da Elipse",base,"x",altura,"=", round(resultado,1))
    else:
        print("Forma invalida")


print("------------------------------")
calc_area (10,2,1)
print("------------------------------")
calc_area (10,5,2)
print("------------------------------")
calc_area (10,5,3)
print("------------------------------")
calc_area (10,5,4)
print("------------------------------")
=======
# Função que calcula o IMC de uma pessoa
def calc_imc(peso, altura):
    return peso / altura ** 2

# p = 85
# a = 1.72
# imc = calc_imc(p, a)

# print(imc)

print(calc_imc(85, 1.72))

################################################

from math import pi

"""
    Função que calcula a área de uma figura geométrica plana
"""
def calc_area(base, altura, tipo):
    if tipo == "R":     # Retângulo
        resultado = base * altura
    elif tipo == "T":   # Triângulo
        resultado = base * altura / 2
    elif tipo == "E":   # Elipse
        resultado = (base / 2) * (altura / 2) * pi
    else:   # Forma inválida ou desconhecida
        resultado = None

    return resultado

print("Retângulo 20x30: ", calc_area(20, 30, "R"))
print("Triângulo 45x32: ", calc_area(45, 32, "T"))
print("Elipse 10x15: ", calc_area(10, 15, "E"))
print("Desconhecido 12x16: ", calc_area(12, 16, "X"))
>>>>>>> bf396c8511a31d8f384ba0f6596bc7756ab7d6ae
