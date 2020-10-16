# 052 - Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
num = int(input('Digiete um número para saber se ele é um número primo: '))
total = 0
for c in range(1, num+1):
    if num % c == 0:
        print('\33[32m', end=' ')
        total += 1
    else:
        print('\33[31m', end=' ')
    print('{}'.format(c), end=' ')
print('\n\33[mO número {} foi devisivel {}° vezes.'.format(num, total))
if total == 2:
    print('Por isso ele é um número primo')
else:
    print('E por isso ele não é um número primo.')
