# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
import sys

# Conversor
def Conversor(m):
    cm = m * 100
    mm = m * 1000
    print('{0} metros corresponde a {1} cm e {2} mm.' .format(m,cm,mm))

op = 's'.upper()
while(op == 'S'):
    m = float(input('\n Informe um valor em metros: '))
    Conversor(m)
    op = input('\n Deseja continuar ? (S = SIM | N = NÃO)').upper()
else:
    print("\n Finalizando...")
    sys.exit()
