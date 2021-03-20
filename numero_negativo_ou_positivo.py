#definindo funções
def banner():
    print("###################################################")
    print("   o numero informado e negativo ou positivo?")
    print("###################################################")
    return

def divisor():
    print("---------------------------------------------------")
    return

def verificacao(x):
    if x > 0:
        print("o número {} é o positivo".format(numero))
        return
    elif x < 0:
        print("o número {} é o negativo".format(numero))
        return
    else:
        print("não temos um número positivo ou negativo, pois 0 e neutro")
        return 

#banner do programa
banner()

#divisor para separar os módulos
divisor()

# declaração de variáveis
numero = float(input("insira um número para realizar o teste: "))

#divisor para separar os módulos
divisor()

# verificação
verificacao(numero)
divisor()