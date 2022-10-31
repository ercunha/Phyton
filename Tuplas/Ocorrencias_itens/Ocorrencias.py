#Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em um tupla;
#Mostre quantas vezes apareceu o número 9
#Qual posição aparece a primeira ocorrência do número 3
#Quais foram os números pares
import sys

op = 'S'
while(op =='S'):
    n1 = int(input('Digite o valor de N1: '))
    n2 = 3
    print('O valor de N2 = 3')
    n3 = int(input('Digite o valor de N3: '))
    n4 = int(input('Digite o valor de N4: '))

    #Guardando números em uma tupla
    numeros = (n1,n2,n3,n4)

    ocorrencias = numeros.count(9)
    posicao = numeros.index(3) +1


    print(f'Total de ocorrências do número 9: {ocorrencias} ')
    print(f'Primeira ocorrência de 3 aparece na posição: {posicao}')
    print(f'Os valores pares encontrados na tupla foram: ',end='')
    for i in numeros:
        if (i % 2 == 0):
             print(i, end=' ')

    op = input('Deseja continuar? ').upper()[0]
else:
    print('Saindo da aplicação...')
    sys.exit()
