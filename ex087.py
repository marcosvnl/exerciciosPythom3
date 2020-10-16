# Exercício Python 087: Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha
números = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
par = terceiro = maior = 0

for l in range(0, 3):
    for c in range(0, 3):
        números[l][c] = int(input(f'Digite o valor da posição {l} {c}: '))
        if números[l][c] % 2 == 0:
            par += números[l][c]
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{números[l][c]:^5}]', end='')
    print()
print(f'A soma de todos os valores PARES digitados é: {par}')
for l in range(0, 3):
    terceiro += números[l][2]
print(f'A soma entre os números da terceira colula é: {terceiro}')
for c in range(0, 3):
    if c == 0:
        maior = números[1][c]
    else:
        if números[1][c] > maior:
            maior = números[1][c]
print(f'O maior número da segunda linha é: {maior}')
