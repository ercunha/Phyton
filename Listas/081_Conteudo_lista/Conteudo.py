#Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista.
#A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.
import sys

op = 'S'
while(op =='S'):
    numeros = []
    digitado = 'Sim'
    for i in range(1,7):
        n = int(input('Informe um valor: '))
        #Tratando para que um número não se repita na lista
        if n not in numeros:
            numeros.append(n)
        else:
            print(f'O número {n} já se encontra na lista.')

    #Verificando se o número 5 se encontra na lista
    if 5 in numeros:
        digitado = 'Sim'
    else:
        digitado = 'Não'

    print(f'Total de números digitados:{i}')
    numeros.sort(reverse=True)
    desc = '-'.join(map(str, numeros))
    print(f'Lista em ordem descrescente:{desc}')
    print(f'O número 5 foi digitado e está na lista? {digitado}')

    op = input('Deseja continuar? ').upper()[0]
else:
    print('Saindo...')
    sys.exit()






