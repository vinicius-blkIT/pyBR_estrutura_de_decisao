from cria_banner import banner

nome_programa = "verificador de vogais e consoantes v1.0"

def verificacao(x):
    if x in vogais:
        print("a letra inserida é uma vogal")
        return
    elif x in consoantes:
        print("a letra inserida é uma consoante")
        return
    else:
        print("caracter inválido")
        return 

#banner do programa
banner(nome_programa)

#loop para garantir que so sera analisado um caracter
vogais = ["a","e","i","o","u"]
consoantes = ["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z"]
i = 2
while i >= 2:
    letra = str.lower(input("insira uma letra para realizar o teste: "))
    i = len(letra)

# verificação
verificacao(letra)