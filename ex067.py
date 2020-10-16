# Faça um programa que mostre a tabuada de qualquer número, um de cada vez, para cada valor digitado pelo usário.
# O programa será interrompido quando o número for negativo.
número = conta = mais = 0
while True:
    número = int(input('Digite um número para ver sua TABUADA [digite um número negativo para para]: '))
    if número <= -1:
        break
    for conta in range(1, 11):
        print(f'{número} X {conta} = {número * conta}')
