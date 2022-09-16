# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
import sys


def Conversor(s):
    return s / 35.20


op = 'S'
while(op == 'S'):
    saldo = float(input('\n Informe quantos reais você tem em sua carteira neste momento: '))
    vl_convertido = Conversor(saldo)
    print(' \n Você pode converter seus R$ {0} reais em US$ {1} dólares ' .format(saldo,round(vl_convertido,2)))

    op =  input('\n Deseja converter outro valor?').upper()

else:
    print('Saindo da aplicação ...')
    sys.exit()

