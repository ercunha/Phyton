#Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores
# ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.
import sys

op = 'S'
while op == 'S':
    numeros = []
    pares = []
    impares = []
    for i in range(1,10):
        n = int(input('Informe um valor: '))
        #Se n não existe em números
        if n not in numeros:
            numeros.append(n)
            if n%2==0:
                pares.append(n)
            else:
                impares.append(n)
        else:
            print(f'O número{n} já foi informado.')

    principal = '-'.join(map(str, numeros))
    nPares = '-'.join(map(str, pares))
    nImpares = '-'.join(map(str, impares))

    print('='*30)
    print(f'Conteúdo da lista principal: {principal}')
    print(f'Números pares: {nPares}')
    print(f'Números ímpares: {nImpares}')
    print('=' * 30)
    op = input('Deseja continuar? ').upper()[0]
else:
    print('Saindo...')
    sys.exit()

