from cria_banner import banner

nome_programa = "verifica a média dos alunos v1.0"

def calcula_media():
    global media
    media = (nota1+nota2+nota3)/3
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

banner(nome_programa)

nota1 = float(input("insira a primeira nota: "))
nota2 = float(input("insira a segunda nota: "))
nota3 = float(input("insira a terceira nota: "))


# verificação
calcula_media()
verificacao(media)