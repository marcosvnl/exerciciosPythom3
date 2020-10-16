# 019 Um professor quer sorear um dos seus 4 alunos para apagar o quadro. Faça em progrma que ajude ele,
# lendo o nome deles e escrevendo o nome do escolhido.
import random
a1 = str(input('Nome do aluno: '))
a2 = str(input('Nome do aluno: '))
a3 = str(input('nome do aluno: '))
a4 = str(input('nome do aluno: '))
print('O sorteado foi: {}!'.format(random.choice([a1, a2, a3, a4])))
# para o Python uma lista deve estar dentro de [].