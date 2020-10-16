def tabuada(num=1):
    """
    Função para escrever a tabuada do número desejado
    :param num: multiplicador desejado
    :return: número a ser multiplicado
    """
    for c in range(1, 11):
        m = num * c
        print(f'{n} x {c:>2} = {m:>2}')
    return n


n = int(input('Tabuada do '))
tabuada(n)
