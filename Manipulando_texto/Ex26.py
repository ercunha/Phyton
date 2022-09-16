#Exercício Python 26: Faça um programa que leia uma frase pelo teclado e
# mostre quantas vezes aparece a letra “A”, em que posição ela aparece a
# primeira vez e em que posição ela aparece a última vez.
import sys

op = 'S'
while(op == 'S'):
    frase = input('Digite uma frase ').upper().strip()
    primeira = frase.find('A')
    ultima = frase.rfind('A')
    print('Total de caracteres = {}' .format(len(frase)))
    print('A letra [A] aparece {} vezes na frase {} ' .format(frase.count('A'),frase))
    print('Primeria ocorrência de [A] no Index: {} ' .format(primeira))
    print('Última ocorrência de [A] no Index: {} ' .format(ultima))

    op = input('\n Deseja informar outra cidade?  ').upper()
else:
    print('Saindo...')
    sys.exit()