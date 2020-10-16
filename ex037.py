# 037 Escreva um porgrama que leia um número inteiro qualquer e e peça para o usuário escolher
# qual será a base de conversão:
# - 1 p/ binário
# - 2 p/ octal
# - 3 p/ hexadecimal
num = int(input('Digite um número inteiro: '))
print('''Você gostaria de converter para qual base a baixo:
[1] para binário
[2] para octal
[3] para hexadecimal''')
esc = int(input('Escolha uma opção: '))
if esc == 1:
    print('O valor {} em BINÁRIO é {}'.format(num, bin(num)[2:]))
elif esc == 2:
    print('O valor {} em OCTAL é {}'.format(num, oct(num)[2:]))
elif esc == 3:
    print('O valr {} em HEXADECIMAL é {}'.format(num, hex(num)[2:]))


