def contador(i, f, p):
    """
    Função para contagem na tela.
    :param i: inicio da comtagem
    :param f: fim da contagem
    :param p: passo da comtagem
    :return: sem retorno
    """
    c = p
    while c <= f:
        print(f'{c}', end=' ')
        c += p
    print('Fim')


contador(0, 10, 2)


# escopos variáveis:


def fatorial(num=1):
    f = 1
    for c in range(num, 1, -1):
        f *= c
    return f


n = (int(input('Digite um número: ')))
print(f'O fatorial de {n} é {fatorial(n)}.')
