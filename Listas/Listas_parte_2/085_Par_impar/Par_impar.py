#Exercício Python 085: Crie um programa onde o usuário possa digitar sete valores numéricos e
# cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final,
# mostre os valores pares e ímpares em ordem crescente.
import sys

op = 'S'
while op == 'S':
    numeros = [[],[]]
    for i in range(1,8):
        v = int(input(f'Informe o valor de N{i}: '))
        if v % 2 == 0:
            numeros[0].append(v)
        else:
            numeros[1].append(v)

    numeros[0].sort()
    numeros[1].sort()

    print('=' *30)
    print(f'Números pares e ímpares:{numeros} ')
    print('=' *30)
    op = str(input('Deseja continuar? ')).upper()
else:
    print('Saindo...')
    sys.exit()