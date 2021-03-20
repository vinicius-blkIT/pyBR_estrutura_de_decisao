#definindo funções
def banner():
    print("###################################################")
    print("realiza saudação de acordo com o periodo de estudos")
    print("###################################################")
    return

def divisor():
    print("---------------------------------------------------")
    return

def instrucoes():
    print("Abaixo o programa irá solicitar a informação do período de estudos")
    print("favor preencher conforme orientação: M-matutino ou V-Vespertino ou N- Noturno")

def verifica_periodo():
    instrucoes()
    while True:
        i = str.upper(input("insira o periodo conforme a instrução acima: "))
        if i == "M":
            print("bom dia!")
            break
        elif i == "V":
            print("boa tarde!")
            break
        elif i == "N":
            print("boa noite!")
            break
        else:
            print("caracter inválido, favor inserir novamente")
            instrucoes()
            continue
    return

periodos = ["M","V","N"]

banner()
divisor()
verifica_periodo()
divisor()
