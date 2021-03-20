#definindo funções
def banner():
    print("###################################################")
    print("     compara três números e mostra o maior")
    print("###################################################")
    return

def divisor():
    print("---------------------------------------------------")
    return

def verificaca_maior(x,y,z):
    if x > y and x > z:
        print("o número maior é o {}".format(numero_1))
        return
    elif y > x and y > z:
        print("o número maior é o {}".format(numero_2))
        return
    elif z > x and z > y:
        print("o número maior é o {}".format(numero_3))
        return
    else:
        print("não temos um número maior, pois eles são iguais")
        return 

def verificaca_menor(x,y,z):
    if x < y and x < z:
        print("o número menor é o {}".format(numero_1))
        return
    elif y < x and y < z:
        print("o número menor é o {}".format(numero_2))
        return
    elif z < x and z < y:
        print("o número menor é o {}".format(numero_3))
        return
    else:
        print("não temos um número menor, pois eles são iguais")
        return 

#banner do programa
banner()

#divisor para separar os módulos
divisor()

# declaração de variáveis
numero_1 = float(input("insira um número para realizar o teste: "))
divisor()
numero_2 = float(input("insira outro número: "))
divisor()
numero_3 = float(input("insira o terceiro número: "))
divisor()

#divisor para separar os módulos
divisor()

# verificação
verificaca_maior(numero_1, numero_2, numero_3)
verificaca_menor(numero_1, numero_2, numero_3)
divisor()