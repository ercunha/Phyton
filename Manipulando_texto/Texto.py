#fatiamento
#Posição:0  1  2  3  4  5  6  7 8   9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26
#       [O][ ][i][n][t][e][r][ ][é][ ][c][a][m][p][e][a][o][ ][d][o][ ][m][u][n][d][o][.]
frase = 'O inter é campeao do mundo.'

# Fatiando o texto e exibindo caracteres da posição 2 a 17
print('Exibindo fatiamento de caracteres da posição 2 - 17 :', frase[2:17])

#Usando len() [lenght = comprimento]
print("Compimento da frase =  {} caracteres incluindo espaços" .format(len(frase)))

#Usando count() [contador] para descobrir quantas vezes uma letra ou string aparecem no texto/frase
print('A letra E aparace {} vezes na frase [{}]' .format(frase.count('e'),frase))

#Usando count() para descobrir quantas vezes uma letra ou string aparecem no texto/frase considerando da posição 0 - 13 (14 primeiros caracteres)
print('A letra E aparace {} vezes na frase [{}] considerando das posições 0-13' .format(frase.count('e',0,13),frase))

#Usando o find para encontrar a primeira ocorrência da string(palavra) "mundo"
print('A palavra [mundo] aparece na posição {} da frase ' .format(frase.find('mundo')))

#Usando operador  'in' para verificar se existe alguma letra ou string na frase
retorno = 'ao' in frase
print('Existe a string "ao" na frase [{}] ? {} '.format(frase,retorno))

#Usando o 'Replace' para substituir a palavra mundo por Brasil
fraseNova = frase.replace('mundo','Brasil')
print('Frase atual:{} ' .format(frase))
print('Nova frase:{} ' .format(fraseNova))

#Caixa alta 'upper()'
fraseNova = frase.upper()
print('Transformando a frase[{}] em caixa alta:{} '.format(frase,fraseNova))

#Caixa baixa 'lower()'
fraseNova = frase.lower()
print('Transformando a frase[{}] em caixa baixa:{} '.format(frase,fraseNova))

# Transforma somente a primeira letra da frase em caixa alta deixando o resto em minusculo 'capitalize()'
fraseNova = frase.capitalize()
print('Transformando a primeira letra da frase[{}]:{} '.format(frase,fraseNova))

# Transforma somente a primeira letra de cada palavra em caixa alta deixando o resto em minusculo 'title()'
fraseNova = frase.title()
print('Transformando a primeira letra de cada palavra frase[{}] {} '.format(frase,fraseNova))

#'strip()' Remove todos espaços inúteis do início e do final da frase
fraseNova = frase.strip()
print('Remove todos espaços inúteis do início da frase[{}] {} '.format(frase,fraseNova))

#'split()' Quebrando por espaços cada palavra em novas listas com novos indices
fraseNova = frase.split()
print('Quebrando por espaços cada palavra em novas listas com novos indices na frase[{}] {} '.format(frase,fraseNova))

#'join()' Juntando todas as palavras separadas em uma lista
fraseNova = "".join(frase)
print('Juntando todas as palavras separadas : frase[{}] => {} '.format(frase,fraseNova))

fraseNova = "-".join(frase)
print('Juntando todas as palavras separadas por espaço com um novo separador: frase[{}] => {} '.format(frase,fraseNova))


