#definindo funções
def banner():
    print("####################################################")
    print("     calcula aumento baseado no salario atual")
    print("####################################################")
    return

def divisor():
    print("---------------------------------------------------")
    return

def verifica_aumento(salario_atual):
    global percentual_aumento
    if salario_atual <= 280:
        percentual_aumento = 0.2
        return
    elif salario_atual > 280 and salario_atual <=700:
        percentual_aumento = 0.15
        return
    elif salario_atual > 700 and salario_atual <=1500:
        percentual_aumento = 0.1
        return
    elif salario_atual > 1500:
        percentual_aumento= 0.05
        return
    else:
        return

    
        
def calcula_aumento(salario, aumento):
    print("o salario atual e R${:.2f}".format(salario))
    print("o percentual de aumento e {}%".format(aumento*100))
    print("o valor do aumento e R${:.2f}".format(salario*aumento))
    print("o novo valor de salario e R${:.2f}".format((salario*aumento)+salario))
    return

divisor()
banner()
divisor()
salario_atual = float(input("insira o valor do salario atual: "))
divisor()
verifica_aumento(salario_atual)
calcula_aumento(salario_atual, percentual_aumento)
divisor()