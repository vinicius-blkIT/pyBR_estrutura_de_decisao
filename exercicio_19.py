from cria_banner import banner

nome_programa = "verificador da estrutura de um número v1.0"

def verifica_unidade(dezenas):
    unidades = numero_a_analisar - ((centenas*100) + (dezenas*10))
    if unidades == 0:
        print("o número não possui nenhuma unidade!")
        return
    else:
        if unidades == 1:
            print("o número inserido pelo usuário possui {} unidade!".format(unidades))
            return
        else:
            print("o número inserido pelo usuário possui {} unidades!".format(unidades))
            return
    return

def verifica_dezena(centenas):
    dezenas = numero_a_analisar - (centenas*100)
    dezenas = dezenas//10
    if dezenas == 0:
        print("o número não possui nenhuma dezena!")
        verifica_unidade(dezenas)
        return
    else:
        if dezenas == 1:
            print("o número inserido pelo usuário possui {} dezena!".format(dezenas))
            verifica_unidade(dezenas)
            return
        else:
            print("o número inserido pelo usuário possui {} dezenas!".format(dezenas))
            verifica_unidade(dezenas)
            return
    return
    


def verifica_estrutura():
    while True:
        global numero_a_analisar
        global centenas
        numero_a_analisar = int(input("insira um número a ser analisado conforme as instruções: "))
        if numero_a_analisar < 1000:
            print("verificando as centenas...")
            centenas = numero_a_analisar//100
            if centenas == 0:
                print("o número não possui nenhuma centena!")
                verifica_dezena(centenas)
                return
            else:
                if centenas == 1:
                    print("o número inserido pelo usuário possui {} centena!".format(centenas))
                    verifica_dezena(centenas)
                    return

                else:
                    print("o número inserido pelo usuário possui {} centenas!".format(centenas))
                    verifica_dezena(centenas)
                    return
        else:
            print("ERRO, insira os dados novamente conforme instruções!")
            instrucoes()
            continue
        return
    return

#estrutura do programa
banner(nome_programa)
verifica_estrutura()