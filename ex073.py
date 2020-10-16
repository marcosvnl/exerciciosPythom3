# 073 - Crie uma tupla preenchida com os 20 primeiros colocados da tabela do compeonato Brasileiro de futebol,
# na ordem de colocação. Depois mostre:
# a) Apenas os 5 primeiros colocados.
# b) Os últimos 4 colocados da tabela.
# c) Uma lista com os times em ordem alfabética.
# d) Em que posição na tabela está o time da chapecoense.
times = 'Flamengo', 'Santos', 'Palmeiras', 'Grêmio',\
        'Athletico-PR', 'São Paulo', 'Internacional',\
        'Corinthians','Fotaleza', 'Goiás',\
        'Bahia', 'Vasco da Gama', 'Atlético-MG',\
        'Fluminense', 'Botafogo', 'Cerá',\
        'Cruzeiro', 'CSA', 'Chapecoence', 'Avai'
print(f'Os quatro primeiro colocado{times[:5]}')
print(f'Os quartro ultimos colocados: {times[-4:]}')
print(f'Todos os timas em ordem alfabértica: {sorted(times)}')
print(f'O time da {times[-2]} está em {times.index("Chapecoence") +1}° lugar.')
