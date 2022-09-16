# Faça um programa que leia a largura e a altura de uma parede em metros,
# calcule a sua área e a quantidade de tinta necessária para pintá-la,
# sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

#Calcula area
import sys


def CalculaQuantidadeTinta(b,h):
    return (b*h) / 2


op = 'S'
while(op =='S'):
   b =  float(input('Informe a largura da parede em metros: '))
   h =  float(input('Informe a altura da parede em metros: '))

   total = round(CalculaQuantidadeTinta(b,h))

   print("\n Para pinta uma parede com {0}m de largura e {1}m de altura você precisa de {2} litros de tinta. " .format(b,h,total))

   op = ('\n Deseja continuar calculando ?').upper()
else:
    print("Saindo da aplicação ...")
    sys.exit()