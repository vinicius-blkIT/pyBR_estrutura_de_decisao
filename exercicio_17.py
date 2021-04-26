#definindo funções
from cria_banner import banner

nome_programa = "calculadora de ano bissexto v1.0"

def calcula_ano_bissexto():
    ano = int(input("digite um ano: "))
    if (ano%4 == 0 and ano%100!= 0) or ano%400 == 0:
        print (" O ano {} informado é bissexto".format(ano))
    else:
        print (" O ano {} informado não é bissexto".format(ano))
    return

#início do programa
banner(nome_programa)
calcula_ano_bissexto()