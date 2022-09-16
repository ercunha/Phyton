# Exercício Python 13: Faça um algoritmo que leia o salário de um funcionário
# e mostre seu novo salário, com x % de aumento ou redução.
import sys


def CalculaReajuste(sal, tipo, percentual):
    if(tipo == 'A'):
        return sal + (sal * (percentual/100))
    else:
        return  sal - (sal * (percentual/100))

def ValidaTipo(t):
    while(t != 'A' or t!= 'B'):
        print('Você deve informar (A) - Aumento ou (R) - Redução')
        tipo = input('Informe (A) para aumento salarial ou (B) para redução salarial: ')
        return False
    else:
        return true

op = 'S'
while(op =='S'):
    nome = input('\n Informe o nome do colaborador: ')
    salario = float(input('Informe o salário atual do colaborador: '))
    tipo = input('Informe (A) para aumento salarial ou (B) para redução salarial: ')

    if(ValidaTipo(tipo) == True):
        percentual = float(input('Informe o percentual a ser aplicado: '))
        novo_salario = round(CalculaReajuste(salario,tipo,percentual),2)

        print('O novo salário do colaborador {0} será de R${1} com o reajuste de {2}% ' .format(nome,novo_salario,percentual))

        op = input('\n Você deseja continuar calculando o salário de outro colaborador? ').upper()
else:
    print('Saindo da aplicação ...')
    sys.exit()
