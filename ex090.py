# Exercício Python 090. Faça um programa que leia nome e média de um aluno, guarde também
# a situação em um dicionário. no final, mostre o conteúdo da estrutura na tela
aluno = dict()
aluno['nome'] = str(input('Nome do aluno: '))
aluno['media'] = float(input(f'Media do {aluno["nome"]}: '))
print(f' - Nome: {aluno["nome"]}')
print(f' - Média: {aluno["media"]}')
if aluno['media'] >= 7:
    print(' - Sitiação \033[4;32mAPROVADO\033[m!')
elif 4 <= aluno['media'] < 7:
    print(' - Situação \033[4;33mRECUPERAÇÃO\033[m!')
else:
    print(' - Situação \033[4;31mREPROVADO\033[m!')
