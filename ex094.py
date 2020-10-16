# Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas,
# guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média
pessoa = dict()
pessoas = list()
mulher = list()
maior = list()
cont = 0
soma = media = 0
while True:
    pessoa.clear()
    cont += 1
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo, digite apenas [M ou F]: ')).strip().upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        else:
            print(f'Erro, a opção {pessoa["sexo"]} não é valodo. Digite M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    media = soma / cont
    if pessoa['sexo'] in 'F':
        mulher.append(pessoa.copy())
    if pessoa['idade'] >= media:
        maior.append(pessoa.copy())
    pessoas.append(pessoa.copy())
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar? ')).strip().upper()[0]
    if resposta == 'N':
        break
print(f'A) Quantas pessoas = {cont}')
print(f'B) media  = {media}')
print(f'C) Mulher = {mulher}')
print(f'D) Pessoas acima da média idade: {maior}')
