# Exercício Python 095: Aprimore o desafio 93 para que ele funcione com vários jogadores,
# incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

time = list()
jogador = dict()
gols = 0
jogos = list()
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    partidas = int(input('Qtd. de partidas: '))
    jogos.clear()
    for c in range(0, partidas):
        jogos.append(int(input(f'Qtd. de gols na {c+1}ª partida: ')))
    jogador['gols'] = jogos[:]
    jogador['total'] = sum(jogos)  # soma total de jogos
    time.append(jogador.copy())
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar?[S/N]: ')).strip().upper()[0]
        print('Responda apenas [S/N].')
    if resposta == 'N':
        break
print('='*40)
print('cod.', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('='*40)
for k, v in enumerate(time):
    print(f'{k:>3}', end=' ')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('='*40)
while True:
    select = int(input('Dados de qual jogador mostror? 999 para finalizar.'))
    if select == 999:
        break
    if select >= len(time):
        print(f'Erro! {select} não corresponde a um jogador na lista.')
    else:
        print(f'Dados de {time[select]["nome"]}:')
        for i, g in enumerate(time[select]["gols"]):
            print(f'No jogo {i+1}ª fez {g} gols')
print('<<< VOLTE SEMPRE >>>')
