# Exercício Python 103: Faça um programa que tenha uma função chamada ficha(),
# que receba dois parâmetros opcionais: o nome de um jogador e quantos gols
# ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador,
# mesmo que algum dado não tenha sido informado corretamente.


def ficha(nome='<desconhecido>', gol=0):
    print(f'O jogador {nome}, fez {gol} gol(s) na partida.')


name = str(input('Nome do jogador\nR: '))
goal = str(input('QTD de gols\nR: '))
if goal.isnumeric():
    goal = int(goal)
else:
    goal = 0
if name.strip() == '':
    ficha(gol=goal)
else:
    ficha(name, goal)
