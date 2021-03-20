#definindo funções
def banner():
    print("###################################################")
    print("     compara dois números e mostra o maior")
    print("###################################################")
    return

def divisor():
    print("---------------------------------------------------")
    return

def verificacao(x,y):
    if x > y:
        print("o número maior é o {}".format(numero_1))
        return
    elif y > x:
        print("o número maior é o {}".format(numero_2))
        return
    else:
        print("não temos um número maior, pois eles são iguais")
        return 

#banner do programa
banner()

#divisor para separar os módulos
divisor()

# declaração de variáveis
numero_1 = float(input("insira um número para realizar o teste: "))
divisor()
numero_2 = float(input("insira outro número: "))

#divisor para separar os módulos
divisor()

# verificação
verificacao(numero_1, numero_2)
divisor()
