#007 desenvolva uma programa que leia as duas notas de um aluno, calcule e mostre a sua média.
p1 = float(input('Nota do 1° semestre: '))
p2 = float(input('nota do 2° semestre: '))
s = (p1 + p2)/2
print('A média entre {} e {} é: {:2}'.format(p1, p2, s))

