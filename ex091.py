# Exercício Python 091: Crie um programa onde 4 jogadores
# joguem um dado e tenham resultados aleatórios.
# Guarde esses resultados em um dicionário em Python.
# No final, coloque esse dicionário em ordem, sabendo
# que o vencedor tirou o maior número no dado.
from random import randint
from operator import itemgetter
jogador = {'jogador 1': randint(1, 6),
           'jogador 2': randint(1, 6),
           'jogador 3': randint(1, 6),
           'jogador 4': randint(1, 6),
           }
posição = list
for k, v in jogador.items():
    print(f'O {k} tirou: {v}')
print('Ranking')
posição = sorted(jogador.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(posição):
    print(f'{i+1}º {v[0]} com {v[1]} pts.')
