from cria_banner import banner

nome_programa = "mostrador de dados em ordem decrescente v1.0"

def coleta_dados():
    lista = []
    qtd = int(input("insira quantos números deseja verificar: "))
    for n in range(qtd):
        elemento = int(input('Digite um numero: '))
        lista.append(elemento)

    lista.sort(reverse = True)
    print(lista)
    return

banner(nome_programa)
coleta_dados()
