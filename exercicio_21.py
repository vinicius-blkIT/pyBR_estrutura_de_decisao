""" from cria_banner import banner

nome_programa = "simulador caixa eletrônico v1.0"

def coleta_valor_saque():
    valor_saque = int(input("insira o valor do saque: "))
    return valor_saque

def valida_saque(valor_saque):
    if valor_saque>=10 and valor_saque <= 600:
        verifica_notas_disponiveis(valor_saque)
        return
    else:
        print("Valor não permitido, favor inserir o valor novamente!")
        coleta_valor_saque()
        return

def verifica_notas_disponiveis(valor_saque): """

numero = int(input('Valor para sacar [10-600]: '))

cem = int(numero / 100)
numero = numero % 100
    
cinquenta = int(numero/50)
numero = numero % 50

dez = int(numero/10)
numero = numero % 10

cinco = int(numero/5)
numero = numero % 5

um = numero
    
print('Notas R$100,00 = ',cem)
print('Notas R$ 50,00 = ',cinquenta)
print('Notas R$ 10,00 = ',dez)
print('Notas R$  5,00 = ',cinco)
print('Notas R$  1,00 = ',um)