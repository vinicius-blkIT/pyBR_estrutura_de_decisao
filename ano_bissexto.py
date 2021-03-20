#definindo funções
def banner():
    print("###################################################")
    print("             calcula ano bissexto")
    print("###################################################")
    return

def divisor():
    print("---------------------------------------------------")
    return

def calcula_ano_bissexto():
    ano = int(input("digite um ano: "))
    if (ano%4 == 0 and ano%100!= 0) or ano%400 == 0:
        print (" O ano {} informado é bissexto".format(ano))
    else:
        print (" O ano {} informado não é bissexto".format(ano))
    return

#banner do programa
banner()

#início do programa
divisor()
calcula_ano_bissexto()
divisor()