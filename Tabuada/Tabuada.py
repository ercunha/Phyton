# Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.
import sys


def Calcula(numero,ate):
    max = ate+1
    for i in range(max):
        print('{0} X {1} = {2}' .format(numero,i,i*numero))

op = 'S'
while(op== 'S'):
    numero = int(input('\n Informe o número que deseja retornar a tabuada: '))
    ate = int(input('Informe o último valor a ser calculado na tabuada: '))

    print(Calcula(numero,ate))

    op = input('\n Deseja calcular a tabuada de outro número? ').upper()
else:
    print("Saindo da aplicação...")
    sys.exit()