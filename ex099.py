# Exercício Python 099: Faça um programa que tenha uma função chamada maior(),
# que receba vários parâmetros com valores inteiros. Seu programa tem que
# analisar todos os valores e dizer qual deles é o maior.


def maior(*número):
    mais = cont = 0
    print(f'\nValores selecionados são: {número}')
    for num in número:
        if num == 1:
            mais = num
        else:
            if num > mais:
                mais = num
        cont += 1
    print(f'Total de valores informados: {cont}')
    print(f'O maior valor: {mais}!')


maior(1, 2, 3, 8, 5)
maior(10, 3)
maior(1, 6, 9, 2, 3, 0)
maior()
