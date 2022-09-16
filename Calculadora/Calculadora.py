#Criando uma calculadora em Python
import math
import sys

n1 = float(input('Digite um valor '))
subtotal = n1
def calcular(subtotal,n2,op):

    # Se for o primeiro cálculo
    if (subtotal == 0):
        # Se for adição
        if (op == '+'):
            subtotal = (n1 + n2)
            return subtotal

        # Se for subtração
        if (op == '-'):
            subtotal = (n1 - n2)
            return subtotal

        # Se for uma divisão
        if(op == '/'):
            subtotal = (n1/n2)
            return subtotal

        # Se for multiplicacao
        if(op == '*'):
            subtotal = n1*n2
            return subtotal
    if (subtotal > 0):
        # Se for adição
        if (op == '+'):
            subtotal = (subtotal + n2)
            return subtotal

            # Se for subtração
        if (op == '-'):
            subtotal = (subtotal - n2)
            return subtotal

            # Se for uma divisão
        if (op == '/'):
            subtotal = (subtotal/n2)
            return subtotal

            # Se for multiplicacao
        if (op == '*'):
            subtotal = (subtotal * n2)
            return subtotal
        #Se for raiz
        if (op == '**'):
            subtotal = math.sqrt(subtotal)
            return subtotal

op = input('Operação')
if (op == '='):
    print('Total calculado => {0} '.format(subtotal))
    sys.exit()

while(op != '='):
    # Se for raiz quadrada
    if(op =='**'):
        subtotal = calcular(subtotal, n2, op)
        print('Total => {0}  '.format(subtotal))
        op = input('Operação')
    else:
        n2 = float(input('Digite um valor '))
        subtotal = calcular(subtotal, n2, op)
        print('Total => {0}  '.format(subtotal))
        op = input('Operação')





