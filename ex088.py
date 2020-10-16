# Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA
# a criar palpites.O programa vai perguntar quantos jogos serão gerados e
# vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em
# uma lista composta.
from random import randint
from time import sleep
lista = list()
jogos = list()
print(30 * '\033[1;32m-=\033[m')
print('                    Jogo da Mega Sena')
print(30 * '\033[1;33m-=\033[m')
qtd = int(input('Quantos jogos você quer fazer? '))
total = 1
while total <= qtd:
    conta = 0
    while True:
        n = randint(0, 60)
        if n not in lista:
            lista.append(n)
            conta += 1
        if conta >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total += 1
for i, l in enumerate(jogos):
    print(f'Jogo - {i+1:>2}: {l}')
    sleep(1)
