# Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos e
# guarde tudo em uma lista composta. No final, mostre um boletim contendo a
# média de cada um e permita que o usuário possa mostrar as notas de cada aluno
# individualmente.
lisgeral = []
while True:
    nome = str(input('Nome do aluno: '))
    n1 = float(input('1ª NOTA: '))
    n2 = float(input('2ª NOTA: '))
    media = (n1 + n2) / 2
    lisgeral.append([nome, [n1, n2], media])
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Cadastrar novo aluno? [S/N]: ')).strip().upper()[0]
    if resposta == 'N':
        break
print(30*'-+')
for i, aluno in enumerate(lisgeral):
    print(f'{i:>2} - {aluno[0]:<10} {aluno[2]:>10.2f}')
print(30*'-+')
escolha = 0
while True:
    print('Digite apenas o número do aluno.')
    escolha = int(input('Ver nota de qual alono [999 para finalizar pesquisa]: '))
    print(30*'-+')
    if escolha == 999:
        break
    if escolha <= len(lisgeral):
        print(f'Note de {lisgeral[escolha][0]}, são: {lisgeral[escolha][1]}')
