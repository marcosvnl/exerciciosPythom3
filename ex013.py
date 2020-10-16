# 013 Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
salario = float(input('Salario do funcionario: '))
acréssimo = salario * 0.15
print('O novo Salario de funcionario de de {:.2f} com 15% de almento!'.format(acréssimo + salario))
