#definindo funções
def banner():
    print("###################################################")
    print("   calcula a media para aprovação dos alunos")
    print("###################################################")
    return

def instrucoes():
    print("###################################################")
    print(" insira as notas de 2 semestres para obter a média")
    print(" baseado na média será exibido o conceito")
    print(" que irá definir a aprovação ou não do aluno")
    print("###################################################")
    return

def divisor():
    print("---------------------------------------------------")
    return

def imprime_medias(media_1, media_2, media_semestre, conceito):
    print("A nota do seu primeiro bimestre foi {:.1f} e a do segundo foi {:.1f}".format(media_1, media_2))
    print("A sua média é {} e o seu conceito é {}".format(media_semestre, conceitos[conceito]))
    if conceito >=0 and conceito <=2:
        print("Você foi APROVADO!")
    elif conceito >=3 and conceito <=4:
        print("Você foi REPROVADO!")
    else:
        print("Média Inválida")
    return

def fim_do_programa():
    print("FIM DO PROGRAMA")

def inserir_medias():
    global media_1
    global media_2
    media_1 = float(input("insira primeira média: "))
    media_2 = float(input("insira segunda média: "))
    return

def verificacao():
    inserir_medias()
    while True:
        if media_1 <=10 and media_2 <=10:
            media_semestre = (media_1 + media_2)/2
            if media_semestre >=9 and media_semestre <=10:
                conceito = 0
                imprime_medias(media_1, media_2, media_semestre, conceito)
                break
            elif media_semestre >=7.5 and media_semestre < 9:
                conceito = 1
                imprime_medias(media_1, media_2, media_semestre, conceito)
                break
            elif media_semestre >=6 and media_semestre < 7.5:
                conceito = 2
                imprime_medias(media_1, media_2, media_semestre, conceito)
                break
            elif media_semestre >=4 and media_semestre < 6:
                conceito = 3
                imprime_medias(media_1, media_2, media_semestre, conceito)
                break
            elif media_semestre >=0 and media_semestre < 4:
                conceito = 4
                imprime_medias(media_1, media_2, media_semestre, conceito)
                break
            else:
                divisor()
                inserir_medias()
                divisor()
                continue
        else:
            divisor()
            print("FAVOR INSERIR VALORES VÁLIDOS!")
            divisor()
            inserir_medias()
        continue
    return
    
#banner do programa
banner()

#divisor para separar os módulos
divisor()

# início do programa
instrucoes()
conceitos = ["A","B","C","D","E"]

#divisor para separar os módulos
divisor()

# verificação
verificacao()
divisor()
fim_do_programa()