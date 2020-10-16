# Exercício Python 086: Crie um programa que declare uma matriz de dimensão 3x3 e preencha
# com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.

números = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        números[l][c] = int(input(f'Digite o valor da posição {l} {c}: '))
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{números[l][c]:^5}]', end='')
    print()
