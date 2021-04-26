from cria_banner import banner

nome_programa = "comparador de dois números v1.0"

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
banner(nome_programa)

numero_1 = float(input("insira um número para realizar o teste: "))
numero_2 = float(input("insira outro número: "))

# verificação
verificacao(numero_1, numero_2)
