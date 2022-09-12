#Escreva um programa que converta uma temperatura digitando em graus Celsius
# e converta para graus Fahrenheit.
import sys


def Converter(temp,tipo):
    if tipo == 'F':
        return (temp-32) * (5/9)
    else:
        return (temp *1.8) +32

def SetTipo(tipo):
    if tipo == 'F':
        return 'C'
    else:
        return 'F'

op = 'S'
tipo = input('Informe [F] para converter fahrenheit para Celsius ou [C] para o contrário: ').upper()
while(op == 'S'):

    while (tipo == 'F' or tipo =='C'):
        tipo = input('Confirme com [F] para converter fahrenheit para Celsius ou [C] para o contrário: ').upper()
        temp = float(input('Informe a temperatura atual: '))
        conversao = Converter(temp,tipo)

        print('{0}º{1} equivale a {2}º{3} '.format(temp,tipo,conversao,SetTipo(tipo)))
        op = input('\n Desaja continuar realizando conversão ? ').upper()
        if op == 'N':
            print('Saindo da aplicação ...')
            sys.exit()
    else:
        tipo = input('Informe [F] para converter fahrenheit para Celsius ou [C] para o contrário: ').upper()
