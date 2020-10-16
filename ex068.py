# Faça um programa que jogue par ou impar com o computador. O jogo só será interrompido quando o jogador perder,
# mostre o total de vitórias consecutivas que ele conquistou no final do jogo
from random import randint
vitoria = 0
print(10 * '-=-')
print('Jogo Par ou Impar')
print(10 * '-=-')
while True:
    jogador = int(input('digite um número:'))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Imapar [P/I]')).upper().strip()[0]
    print(f'Você esconheu o número {jogador} e o computador jogou {computador} o total foi {total}',end=' ')
    print('deu par' if total % 2 == 0 else 'deu impar')
    if tipo == 'P':
        if total % 2 == 0:
            vitoria += 1
            print('Parabéns você galhou!')
        else:
            print('Você perdeu')
            break
    if tipo == 'I':
        if total % 2 == 1:
            vitoria += 1
            print('Parabéns você ganhou!')
        else:
            print('Você perdeu')
            break
    print('Vamos joar de novo!')
print(f'Game Over! Você teve {vitoria} vitorias.')