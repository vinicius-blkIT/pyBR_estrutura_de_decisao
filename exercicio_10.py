from cria_banner import banner

nome_programa = "saudação de acordo com o período de estudos v1.0"

def verifica_periodo():
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

banner(nome_programa)
verifica_periodo()
