# Tabuada
import sys

# Realiza o calculo da tabuada
def CalcularTabuada(numero,max):
    for i in range(max+1):
        multiplicacao = numero*i
        print('{0} x {1} = {2} ' .format(numero,i,multiplicacao))

#Força a primeira entrada no laço de repetição
op = 'S'

# Enquanto a resposta for s repete o laço
while(op == 'S'):
    numero = int(input('\n Informe o número que quer saber a tabuada: '))
    max = int(input('Informe o valor máximo que deseja saber: ' ))
    CalcularTabuada(numero,max)

    op = input('\n Deseja calcular a tabuada de outro número ? ').upper()

# Se não, finaliza o programa
else:
    print("\n Finalizando...")
    sys.exit()


