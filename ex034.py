# 034 Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# para salários acima de 1250,00 calcule aumento de 10%.
# Para salários inferiores ou igual, o aumento é de 15%.
salario = float(input('Digite seu salario atual R$'))
if salario <= 1250:
    print('Seu salário com 15% de aumento: R${:.2f}'.format((salario*0.15 + salario)))
if salario > 1250:
    print('Seu salário com 10% de aumento: R${:.2f}'.format((salario*0.10 + salario)))
