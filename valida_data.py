#definindo funções
def banner():
    print("###################################################")
    print("          verifica se uma data é válida")
    print("###################################################")
    return

def divisor():
    print("---------------------------------------------------")
    return

def verifica_dia():
    global dia
    dia = int(input("insira o dia: "))
    if dia <= max_dia:
        print("O dia {} é válido.".format(dia))
        print("A data {}/{}/{} é válida!".format(dia, mes, ano))
        return   
    else:
        print("dia inválido, encerrando o programa")
        return

def verifica_mes():
    global mes
    mes = int(input("insira o mes: "))
    global max_dia
    if mes <= 12:
        if mes in meses_com_31_dias:
            max_dia = 31
            print("O mês {} é válido.".format(mes))
            verifica_dia()
            return 
        elif mes in meses_com_30_dias:
            max_dia = 30
            print("O mês {} é válido.".format(mes))
            verifica_dia()
            return 
        else:
            max_dia = fevereiro
            print("O mês {} é válido.".format(mes))
            verifica_dia()
            return 
    else:
        print("mês inválido, encerrando o programa")
        return
    return 

def verifica_ano():
    global ano
    ano = int(input("insira o ano: "))
    global fevereiro
    if ano >= 0:    
        if (ano%4 == 0 and ano%100!= 0) or ano%400 == 0:
            print ("O ano {} é válido e bissexto".format(ano))
            fevereiro = 29
            verifica_mes()
            return
        else:
            print ("O ano {} é válido e não é bissexto".format(ano))
            fevereiro = 28
            verifica_mes()
            return
    else:
        print("ano inválido, encerrando o programa")
        return
    return

#banner do programa
banner()

#início do programa
divisor()
meses_com_31_dias = [1,3,5,7,8,10,12]
meses_com_30_dias = [4,6,9,11]
verifica_ano()
divisor()