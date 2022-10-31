#Crie um programa que tenha uma tupla com várias palavras.
#Depois disso, mostrar as vogais de cada palavra.
import sys

op = 'S'
while(op =='S'):

    p1 = input('Digite uma palavra: ').lower()
    p2 = input('Digite uma palavra: ').lower()
    p3 = input('Digite uma palavra: ').lower()
    p4 = input('Digite uma palavra: ').lower()
    palavras = p1,p2,p3,p4

    for p in palavras:
        print(f'\n Na palavra {p} temos as vogais: ',end='')
        for letra in p:
            if(letra in 'aeiou'):
                print(letra, end=' ')

    op = input('\n Deseja continuar? ').upper()[0]
else:
    print('Saindo...')
    sys.exit()

