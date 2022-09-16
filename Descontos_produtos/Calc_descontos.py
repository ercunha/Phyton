# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
import sys


def Calcula(valor,desconto):
    return valor - (valor * (desconto/100))

op = 'S'
while(op == 'S'):
    prod = input('\n Informe o nome do produto: ')
    val =  float(input('Informe o valor do produto: '))
    desc = float(input('Informe o desconto a ser considerado: '))
    valorAtualizado = round(Calcula(val,desc),2)

    print('Valor anterior do produto {0} era de R${1}' .format(prod,round(val)))
    print('Valor atualizado do produto {0} é de R${1}' .format(prod,valorAtualizado))

    op = input('\n Deseja continuar calculando? ').upper()
else:
    print('Saindo da aplicação ...')
    sys.exit()