lanches = ('Hamburguer','Suco','Pizza','Sorvete')
print(lanches)

#Percorrendo a tupla e imprimindo dados

for c in lanches:
    print(f'{c}')

print('='*30)
print('{:^30}'.format('USANDO RANGE'))
print('=' * 30)
for cont in range(0,len(lanches)):
    print(f'Posição[{cont}] = {lanches[cont]}')

print('='*30)
print('{:^30}'.format('USANDO ENUMERATE'))
print('=' * 30)
for cont,c in enumerate(lanches):

    print(f'Posição[{cont}] =>{c}')

print('='*30)
print('{:^30}'.format('ORDEM ALFABÉTICA'))
print('=' * 30)
print(sorted(lanches))

print('='*30)
print('{:^30}'.format('UNINDO TUPLAS COM SINAL DE +'))
print('=' * 30)
a = (2,4,5)
b = (6,8,5)
c = b+a

print(a)
print(b)
print(c)

print('='*30)
print('{:^30}'.format('QUANTIDADE DE OCORRÊNCIAS DE UM DETERMINADO ELEMENTO'))
print('='*30)
print(f'O número (5) aparece {c.count(5)} vezes.')


