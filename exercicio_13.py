from cria_banner import banner

nome_programa = "informa dia da semana v1.0"

def fim_do_programa():
    print("FIM DO PROGRAMA")

def verificacao(dia_da_semana):
    if dia_da_semana in range(len(dias_da_semana)):
        print("o dia da semana selecionado é {}".format(dias_da_semana[dia_da_semana]))
    else:
        print("favor inserir um valor inválido")
    return

#banner do programa
banner(nome_programa)

# declaração de variáveis
dia_selecionado = int(input("insira o número desejado: "))
dia_selecionado = dia_selecionado - 1
dias_da_semana = ["Domingo", "Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado"]

# verificação
verificacao(dia_selecionado)