from cria_banner import banner

nome_programa = "verificador de sexo v1.0"

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
banner(nome_programa)

# declaração de variáveis
sexo = str.upper(input("insira o sexo do usuario M, masculino e F, feminino : "))
masculino = "M"
feminino = "F"

# verificação
verificacao(sexo)