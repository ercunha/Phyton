# Escreva um programa que pergunte a quantidade de Km percorridos por um
# carro alugado e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
import sys


def Calcula(km,dias):
    return (dias*60) +(km*0.15)

op = 'S'
while(op =='S'):

    dias = int(input('\n Informe a quantidade de dias que o carro foi utilizado: '))
    km = float(input('Informe a KM percorrida: '))
    valor = round(Calcula(km,dias),2)
    print('Valor do aluguel de {0} dias e {1}km percorridos = R${2}' .format(dias,km,valor))
    op =input('\n Deseja continuar calculando? ').upper()
else:
    print('Saindo da aplicação...')
    sys.exit()