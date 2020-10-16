# 020 O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos
# alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
import random
a1 = str(input('1° aluno: '))
a2 = str(input('2° aluno: '))
a3 = str(input('3° aluno: '))
a4 = str(input('4° aluno: '))
lista = [a1, a2, a3, a4]
random.shuffle(lista)
print('Ordem de apresentação!')
print(lista)
