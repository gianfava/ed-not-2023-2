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
