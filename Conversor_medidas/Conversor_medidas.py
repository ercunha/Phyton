#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
import sys


def Converter(valor):
    cm = valor*100
    mm = valor*1000
    return "\n {0}m equivale a {1} cm ou {2} mm. " .format(valor,cm,mm)

op = 'S'
while(op =='S'):
    valor = float(input('\n Informe o valor em metros a ser convertido: '))
    print(Converter(valor))

    op = input("\n Deseja continuar calculando outro valor? [S = Sim ou N = não] ").upper()
else:
    print("Saindo da aplicação...")
    sys.exit()