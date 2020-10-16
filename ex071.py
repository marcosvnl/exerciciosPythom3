# Crie um Programa que simule um funcionamento de um caixa eletrônico. no início, pergunte ao usuário qual
# será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão
# entregues - Considere que o caixa possui cédulas de [50, 20, 10 e 1]
print('~' * 40)
print('{:^40}'.format('BANCO X'))
print('~' * 40)
saque = int(input('Digite o valor a ser sacado: R$'))
total = saque
cédula = 50
totalcédula = 0
while True:
    if total >= cédula:
        total -= cédula
        totalcédula += 1
    else:
        if totalcédula > 0:
            print(f'{totalcédula} cédulas de {cédula}')
        if cédula == 50:
            cédula = 20
        elif cédula == 20:
            cédula = 10
        elif cédula == 10:
            cédula = 1
        totalcédula = 0
        if total == 0:
            break
print('{:^40}'.format('Obrigado por utilizar nossos serviços'))
print('{:^40}'.format('Volte sempre'))
