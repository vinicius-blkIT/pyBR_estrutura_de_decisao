#definindo funções
def banner():
    print("###################################################")
    print("     informa o sexo selecionado pelo usuario")
    print("###################################################")
    return

def divisor():
    print("---------------------------------------------------")
    return

def verificacao(x):
    if x == masculino:
        print("o sexo informado é masculino")
        return
    elif x == feminino:
        print("o sexo informado é feminino")
        return
    else:
        print("dados invalidos, favor reiniciar")
        return 

#banner do programa
banner()

#divisor para separar os módulos
divisor()

# declaração de variáveis
sexo = str.upper(input("insira o sexo do usuario M, masculino e F, feminino : "))
masculino = "M"
feminino = "F"

#divisor para separar os módulos
divisor()

# verificação
verificacao(sexo)
divisor()