# Exercício Python 104: Crie um programa que tenha a função leiaInt(),
# que vai funcionar de forma semelhante 'a função input() do Python,
# só que fazendo a validação para aceitar apenas um valor numérico.
# Ex: n = leiaInt('Digite um n: ')


def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        num = str(input(msg))
        if num.isnumeric():
            valor = int(num)
            ok = True
        else:
            print('\33[1;31mERRO! <dado invalido>\nDigite apenas números inteiros.\33[m')
        if ok:
            break
    return valor


n = leiaInt('Digite um número: ')
print(f'{n} é um número inteiro.')
