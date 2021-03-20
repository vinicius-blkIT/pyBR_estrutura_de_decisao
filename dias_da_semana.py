#definindo funções
def banner():
    print("###################################################")
    print("     compara dois números e mostra o maior")
    print("###################################################")
    return

def instrucoes():
    print("###################################################")
    print(" insira um numero de 1 a 7 para que seja exibido")
    print(" o dia da semana correspondente ao número")
    print("###################################################")
    return

def divisor():
    print("---------------------------------------------------")
    return

def fim_do_programa():
    print("FIM DO PROGRAMA")

def verificacao(dia_da_semana):
    if dia_da_semana in range(len(dias_da_semana)):
        print("o dia da semana selecionado é {}".format(dias_da_semana[dia_da_semana]))
    else:
        print("favor inserir um valor inválido")
    return

#banner do programa
banner()

#divisor para separar os módulos
divisor()



# declaração de variáveis
instrucoes()
dia_selecionado = int(input("insira o número desejado: "))
dia_selecionado = dia_selecionado - 1
dias_da_semana = ["Domingo", "Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado"]

#divisor para separar os módulos
divisor()

# verificação
verificacao(dia_selecionado)
divisor()
fim_do_programa()