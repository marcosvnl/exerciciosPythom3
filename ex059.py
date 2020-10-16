# Crie um programa queleia dois valores e mostre um menu na tela:
# [1] - Somar
# [2] - multiplicar
# [3] - Maior
# [4] - Novos números
# [5] - Sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso
from time import sleep
num1 = int(input('Digite o 1° valor: '))
num2 = int(input('Digite o 2° valor: '))
escolha = 0
mais = 0
while escolha != 5:
    print('''Escolha uma das opções abaixo:
[1] - Somar
[2] - Multiplicar
[3] - Número maior
[4] - Novos números
[5] - Sair do programa''')
    escolha = int(input('Opção: '))
    if escolha > 6:
        print('\33[1;31mOpção invalida! escolha uma da opções acima.\33[m')
    elif escolha == 1:
        soma = num1 + num2
        print('A soma entre {} e {} é igual a {}'.format(num1, num2, soma))
    elif escolha == 2:
        mult = num1 * num2
        print('A multiplicação entre {} e {} é igual a {}'.format(num1, num2, mult))
    elif escolha == 3:
        if num1 > num2:
            print('O maior valor é {}'.format(num1))
        else:
            print('O maior valor é {}'.format(num2))
    elif escolha == 4:
        print('\33[1;34mNovos valores\33[m')
        num1 = int(input('Digite o 1° valor: '))
        num2 = int(input('Digite o 2° valor: '))
    elif escolha == 5:
        print('Finalizando')
        sleep(5)
    print(15*'-=')
