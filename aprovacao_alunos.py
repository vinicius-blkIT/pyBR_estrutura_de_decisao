#definindo funções
def banner():
    print("###################################################")
    print("             aprovado ou reprovado?")
    print("###################################################")
    return

def divisor():
    print("---------------------------------------------------")
    return

def calcula_media():
    global media
    media = (nota1 + nota2)/2
    return media


def verificacao(x):
    if x == 10:
        print("aluno aprovado com distincao")
        return
    elif x >= 7:
        print("aluno aprovado")
        return
    else:
        print("aluno reprovado")
        return 

#banner do programa
banner()

#divisor para separar os módulos
divisor()

#loop para garantir que so sera analisado um caracter
nota1 = float(input("insira a primeira nota: "))
nota2 = float(input("insira a segunda nota: "))


#divisor para separar os módulos
divisor()

# verificação
calcula_media()
verificacao(media)
divisor()