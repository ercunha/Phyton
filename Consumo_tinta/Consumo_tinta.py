#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua
# área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta
# pinta uma área de 2 metros quadrados.
import sys


def Calcula(l,h):
    area = l*h
    litros = (l*h) /2
    print('\n Para pintar uma parede de {0}m² será preciso usar {1} litro(s) de tinta.' .format(area,litros))

op = 'S'
while(op =='S'):
    l = float(input('\n Informe a largura da parede: '))
    h = float(input('\n Informe a altura da parede: '))
    Calcula(l,h)
    op = input("\n Deseja continuar calculando outro valor? [S = Sim ou N = não] ").upper()
else:
    print('Saindo da aplicação...')
    sys.exit()