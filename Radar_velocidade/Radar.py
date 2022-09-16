#Exercício Python 29: Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite.
import sys

op = 'S'

#Calcula o valor da multa
def Calcular(v):
    return (v - 80) * 7.00

#Simula o Radar
def SimularRadar(v):
    if v >80:
        multa = Calcular(v)
        print('Veículo foi multado em R$ {} !' .format(multa))
    else:
        print('Veículo OK !')

while(op == 'S'):

    vel = float(input('Informe a velocidade do veículo: '))
    SimularRadar(vel)

    op = input('\n Deseja continuar simulando? ').upper()
else:
    print('Saindo...')
    sys.exit()
