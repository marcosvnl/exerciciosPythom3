# Exercício Python 102: Crie um programa que tenha uma função fatorial()
# que receba dois parâmetros: o primeiro que indique o número a calcular
# e outro chamado show, que será um valor lógico (opcional)
# indicando se será mostrado ou não na tela o processo de cálculo do fatorial.


def fatoral(a, show=False):
    """
    Fatoramento de número
    :param a: Número a farorar
    :param show: True = mostra conta, False = não mostra conta
    :return: f = variavel de fatoramento
    """
    f = 1
    for c in range(a, 0, -1):
        if show:
            print(f'{c}', end='')
            if c > 1:
                print(f' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


fat = int(input('Número á fatorar: '))
resposta = str(input('Mostrar conta e resultado?\nResposta ')).upper().strip()[0]
if resposta == 'N':
    print(fatoral(fat, show=False))
else:
    print(fatoral(fat, show=True))
