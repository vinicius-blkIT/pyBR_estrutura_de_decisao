#definindo funções
def banner():
    print("########################################################")
    print("                     triangulos")
    print("########################################################")
    return

def divisor():
    print("--------------------------------------------------------")
    return

def verifica_triangulo():
    while True:
        lado1 = float(input("insira o primeiro lado:"))
        lado2 = float(input("insira o segundo lado:"))
        lado3 = float(input("insira o terceiro lado:"))
        if lado1-lado2 < lado3 and lado3 < lado1+lado2 and lado1-lado3 < lado2 and lado2 < lado1+lado3 and lado2-lado3 < lado1 and lado1 < lado2+lado3:
            print("É um triângulo!")
            tipifica_triangulo(lado1,lado2,lado3)
            break
        else:
            divisor()
            print("Não é um triângulo, favor inserir os lados novamente!")
            divisor()
            continue
        return

def tipifica_triangulo(lado1, lado2,lado3):
    if lado1 == lado2 and lado1 == lado3:
        print("Triângulo Equilátero")
        return
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("Triângulo Isósceles")
        return
    elif lado1 != lado2 and lado1 != lado3 and lado2 != lado3:
        print("Triângulo Escaleno")
        return
    else:
        print("houve um erro!")
        return
    return


#banner do programa
banner()

#divisor para separar os módulos
divisor()

# verificação
verifica_triangulo()
divisor()