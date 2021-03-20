#definindo funções
def banner():
    print("####################################################")
    print("            calcula salario liquido")
    print("####################################################")
    return

def divisor():
    print("----------------------------------------------------")
    return

def calcula_salario_bruto():
    global salario_bruto
    salario_bruto = horas_trabalhadas*valor_por_hora
    return

def verifica_faixa_ir():
    global percentual_ir
    if salario_bruto <= 900:
        percentual_ir = 0
        return
    elif salario_bruto > 900 and salario_bruto <=1500:
        percentual_ir = 0.05
        return
    elif salario_bruto > 1500 and salario_bruto <=2500:
        percentual_ir = 0.1
        return
    elif salario_bruto > 2500:
        percentual_ir= 0.2
        return
    else:
        return

def calcula_salario_liquido():
    global desconto_ir
    global desconto_inss
    global salario_liquido
    global calculo_fgts
    desconto_ir = salario_bruto*percentual_ir
    desconto_inss = salario_bruto*0.1
    calculo_fgts = salario_bruto*0.11
    descontos = desconto_ir + desconto_inss
    salario_liquido = salario_bruto - descontos
    return

def mostra_info_usuario():
    print("o salario bruto é R${:.2f}".format(salario_bruto))
    if percentual_ir > 0:
        print("o desconto de IR -{:.0f}%- é R${:.2f}".format(percentual_ir*100,desconto_ir))
    else:
        print("para essa faixa salarial não há desconto de IR")
    print("o desconto de INSS -10%- é R${:.2f}".format(desconto_inss))
    print("o valor do FGTS -11%- R${:.2f}".format(calculo_fgts))
    print("o salário líquido é R${:.2f}".format(salario_liquido))
    return

banner()
divisor()

#declarando variaveis
horas_trabalhadas = float(input("insira a quantidade de horas trabalhadas: "))
valor_por_hora = float(input("insira o valor das horas trabalhadas: "))

divisor()

calcula_salario_bruto()
verifica_faixa_ir()
calcula_salario_liquido()
mostra_info_usuario()

divisor()

print("fim do programa")



