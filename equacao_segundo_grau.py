#importando libs
import math

#definindo funções
def banner():
    print("###################################################")
    print("        calcula a equação do segundo grau")
    print("               ax² + bx + c = 0")
    print("###################################################")
    return

def instrucoes():
    print("###################################################")
    print(" insira os coeficientes a, b e c para realizar")
    print(" o cálculo da equação de segundo grau")
    print("###################################################")
    return

def divisor():
    print("---------------------------------------------------")
    return    

def fim_do_programa():
    print("FIM DO PROGRAMA")

def calcula_equacao():
    while True:
        coeficiente_a = float(input("insira o coeficiente - a: "))
        if coeficiente_a==0:
            divisor()
            print("valor do coeficiente -a- inválido, não é uma equação do segundo grau, favor inserir o coeficiente novamente!")
            divisor()
            continue
        else:
            coeficiente_b = float(input("insira o coeficiente - b: "))
            coeficiente_c = float(input("insira o coeficiente - c: "))
            delta = coeficiente_b*coeficiente_b - (4*coeficiente_a*coeficiente_c)
            if delta<0:
                divisor()
                print("Delta menor que 0, portanto não possui raízes reais")
                divisor()
                break
            elif delta==0:
                raiz = -coeficiente_b / (2*coeficiente_a)
                divisor()
                print("Delta=0 , portanto a raiz é única e igual à {}".format(raiz))
                divisor()
                break
            else:
                raiz1 = (-coeficiente_b + math.sqrt(delta) ) / (2*coeficiente_a)
                raiz2 = (-coeficiente_b - math.sqrt(delta) ) / (2*coeficiente_a)
                print("Raizes: {:.2f} e {:.2f}".format(raiz1,raiz2))
                break
        return
    return
    
#banner do programa
banner()

#divisor para separar os módulos
divisor()

# início do programa
instrucoes()

#divisor para separar os módulos
divisor()

# verificação
calcula_equacao()
divisor()
fim_do_programa()