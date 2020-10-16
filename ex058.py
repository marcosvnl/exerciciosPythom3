# 058 - Melhore o jogo do desafio 028 onde o comptador "pensa" em um número de 0 a 10.
# Só que agora o jogador vai tentar adivinhar até acertar, mostre no final quantos palpites foram necessaríos para vencer.
from random import randint
cont = 0
pc = randint(0, 10)
certo = False
print('Vamos jogar.... Estou pensando aqui em um número de 0 à 10!\nVocê é capas de adivinhar?')
while not certo:
    player = int(input('De seu palpite: '))
    cont += 1
    if player == pc:
        certo = True
    else:
        if player < pc:
            print('Maior! Tente outra vez')
        elif player > pc:
            print('Menor! Tente outra vez')
print('Acertou! Você usou {} tentativas para que eu estava com o número {} guardado na memória!'.format(cont, pc))
