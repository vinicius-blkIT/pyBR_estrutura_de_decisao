from cria_banner import banner

nome_programa = "comparador de três produtos v1.0"

def imprime_resultado(produto_mais_barato):
    print("o produto que você deve comprar é {}".format(produto_mais_barato))
    return

def verifica_preco(x,y,z):
    if x < y and x < z:
        imprime_resultado(nome_produto_1)
        return
    elif y < x and y < z:
        imprime_resultado(nome_produto_2)
        return
    elif z < x and z < y:
        imprime_resultado(nome_produto_3)
        return
    else:
        print("ERRO")
        return 

#banner do programa
banner(nome_programa)

# declaração de variáveis
nome_produto_1 = input("insira o nome do produto 1: ")
produto_1 = float(input("insira o valor do {}: ".format(nome_produto_1)))
nome_produto_2 = input("insira o nome do produto 2: ")
produto_2 = float(input("insira o valor do {}: ".format(nome_produto_2)))
nome_produto_3 = input("insira o nome do produto 3: ")
produto_3 = float(input("insira o valor do {}: ".format(nome_produto_3)))
# verificação
verifica_preco(produto_1, produto_2, produto_3)