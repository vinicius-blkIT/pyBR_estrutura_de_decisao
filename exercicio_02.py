from cria_banner import banner

nome_programa = "verificador de sinal v1.0"

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
banner(nome_programa)

# declaração de variáveis
numero = float(input("insira um número para realizar o teste: "))

# verificação
verificacao(numero)