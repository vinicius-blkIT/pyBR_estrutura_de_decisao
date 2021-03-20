#definindo funções
def banner():
    print("###################################################")
    print("             vogal ou consoante?")
    print("###################################################")
    return

def divisor():
    print("---------------------------------------------------")
    return

def verificacao(x):
    if x in vogais:
        print("a letra inserida e uma vogal")
        return
    elif x in consoantes:
        print("a letra inserida e uma consoante")
        return
    else:
        print("caracter invalido")
        return 

#banner do programa
banner()

#divisor para separar os módulos
divisor()

#loop para garantir que so sera analisado um caracter
vogais = ["a","e","i","o","u"]
consoantes = ["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z"]
i = 2
while i >= 2:
    letra = str.lower(input("insira uma letra para realizar o teste: "))
    i = len(letra)

#divisor para separar os módulos
divisor()

# verificação
verificacao(letra)
divisor()