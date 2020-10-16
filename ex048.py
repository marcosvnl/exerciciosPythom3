# 048 - Faça um programa que calcule a soma entre todos os números impares que são mútiplos de três e que
# sem encontram no intervalo de 1 até 500
soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont = cont + 1
        soma += c
print('O somatorio dos {} multiplos de 3, entre 1 a 500 é {}!'.format(cont, soma))
