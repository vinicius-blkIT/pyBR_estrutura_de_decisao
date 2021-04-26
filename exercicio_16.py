#importando libs
import math
from cria_banner import banner

nome_programa = "calculadora de equação do segundo grau v1.0"

def calcula_equacao():
    while True:
        coeficiente_a = float(input("insira o coeficiente - a: "))
        if coeficiente_a==0:
            print("valor do coeficiente -a- inválido, não é uma equação do segundo grau, favor inserir o coeficiente novamente!")
            continue
        else:
            coeficiente_b = float(input("insira o coeficiente - b: "))
            coeficiente_c = float(input("insira o coeficiente - c: "))
            delta = coeficiente_b*coeficiente_b - (4*coeficiente_a*coeficiente_c)
            if delta<0:
                print("Delta menor que 0, portanto não possui raízes reais")
                break
            elif delta==0:
                raiz = -coeficiente_b / (2*coeficiente_a)
                print("Delta=0 , portanto a raiz é única e igual à {}".format(raiz))
                break
            else:
                raiz1 = (-coeficiente_b + math.sqrt(delta) ) / (2*coeficiente_a)
                raiz2 = (-coeficiente_b - math.sqrt(delta) ) / (2*coeficiente_a)
                print("Raizes: {:.2f} e {:.2f}".format(raiz1,raiz2))
                break
        return
    return
    
#banner do programa
banner(nome_programa)

# verificação
calcula_equacao()