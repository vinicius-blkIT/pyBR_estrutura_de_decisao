#definindo funções
def banner():
    print("####################################################")
    print(" coleta números e mostra em ordem decrescente")
    print("####################################################")
    return

def divisor():
    print("---------------------------------------------------")
    return

def coleta_dados():
    lista = []
    qtd = int(input("insira quantos números deseja verificar: "))
    for n in range(qtd):
        elemento = int(input('Digite um numero: '))
        lista.append(elemento)

    lista.sort(reverse = True)
    print(lista)
    return

divisor()
banner()
divisor()
coleta_dados()
divisor()
