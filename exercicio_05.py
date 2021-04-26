from cria_banner import banner

nome_programa = "verifica aprovação de alunos v1.0"

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
banner(nome_programa)

#loop para garantir que so sera analisado um caracter
nota1 = float(input("insira a primeira nota: "))
nota2 = float(input("insira a segunda nota: "))


# verificação
calcula_media()
verificacao(media)
