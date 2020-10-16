# Exercício Python 098: Faça um programa que tenha uma função chamada contador(),
# que receba três parâmetros: início, fim e passo. Seu programa tem que realizar
# três contagens através da função criada:
#
# a) de 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2
# c) uma contagem personalizada

from time import sleep


def contador(ini, fim, de):
    if de == 0:
        de = 1
    if de < 0:
        de *= -1
    print('=+' * 20)
    print(f'Contando de {ini} até {fim} de {de} em {de}')
    if ini < fim:
        c = ini
        while c <= fim:
            print(f'{c} ', end='')
            sleep(0.3)
            c += de
    else:
        c = ini
        while c >= fim:
            print(f'{c} ', end='',)
            sleep(0.3)
            c -= de


contador(1, 10, 1)
print()
contador(10, 0, 2)
print()
print('Pesonalize uma contagem:')
i = int(input('Inicío: '))
f = int(input('Fim: '))
d = int(input('Passo: '))
contador(i, f, d)
