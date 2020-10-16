# Fça um progrma que leia nome e peso de varias pessoas quandando tudo em uma lista.
# No final mostre
# A - Quantas pessoas foram cadastradas
# B - Uma listagem com as pesoas mais pesadas
# C - Uma listagem com as pessoas mais leves
pessoas = list()
dados = list()
maior = menor = 0
qtd = 0
while True:
    dados.append(str(input('Digite o nome: ')))
    dados.append(float(input('Digite o peso: ')))
    if len(pessoas) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    qtd += 1
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer cadastrar mais pessoas? ')).strip().upper()[0]
    if resposta == 'N':
        break
print(f'Você cadastrou {qtd} pessoas')
print(f'O maior peso foi o de {maior}Kg ', end='')
for p in pessoas:
    if maior == p[1]:
        print(f'e é o de {p[0]}Kg', end='')
print(f'\nO menor peso foi o de {menor}Kg ', end='')
for p in pessoas:
    if menor == p[1]:
        print(f'e é o de {p[0]}', end='')
print()
