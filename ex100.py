# Exercício Python 100: Faça um programa que tenha uma lista chamada números
# e duas funções chamadas sorteia() e somaPar(). A primeira função vai
# sortear 5 números e vai colocá-los dentro da lista e a segunda função
# vai mostrar a soma entre todos os valores pares sorteadospela função anterior.

import random
números = list()


def sorteia(lst):
    for c in range(0, 5):
        lst.append(random.randint(1, 10))
    print(f'{números}')


def somaPar(lst):
    soma = 0
    for valor in lst:
        if valor % 2 == 0:
            soma += valor
    print(f'\nA soma entre os números pares da lista:{lst}. É {soma}!')


sorteia(números)
somaPar(números)
