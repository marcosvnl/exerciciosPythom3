# Exercício Python 093: Crie um programa que gerencie o
# aproveitamento de um jogador de futebol. O programa vai
# ler o nome do jogador e quantas partidas ele jogou.
# Depois vai ler a quantidade de gols feitos em cada partida.
# No final, tudo isso será guardado em um dicionário, incluindo
# o total de gols feitos durante o campeonato.

jogador = dict()
gols = 0
jogos = list()
jogador['nome'] = str(input('Nome do jogador: '))
patidas = int(input('Qtd. de partidas: '))
for c in range(0, patidas):
    jogos.append(int(input(f'Qtd. de gols na {c}ª partida: ')))
jogador['gols'] = jogos[:]
jogador['total'] = sum(jogos)  # soma total de jogos
print(30*'-=')
print(jogador)
print(30*'-=')
for k, v in jogador.items():
    print(f'No campo {k} tem o valor {v}')
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} essa temporada.')
for i, v in enumerate(jogos):
    print(f'    => Na partida {i} fez {v} gols.')
