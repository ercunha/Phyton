#Crie um programa que tenha uma tupla totalmente preenchida com uma contagem
# por extenso de zero até vinte. Seu programa deverá ler um número pelo teclado e
# mostra-lo por extenso.
import sys

numeros = ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez',
           'onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito',
           'dezenove','vinte')

op = 'S'
while(op == 'S'):
    n = -1
    while(n<0 or n>20):
     n = int(input('Informe um número de 1 a 20: '))
    print(f'Você digitou o número => {numeros[n]}.')
    op = input('\n Gostaria de informar outro número? ').upper()[0]
else:
    print('Saindo da aplicação...')
    sys.exit()




