# Exercício Python 101: Crie um programa que tenha uma função chamada voto()
# que vai receber como parâmetro o ano de nascimento de uma pessoa,
# retornando um valor literal indicando se uma pessoa tem
# voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.


def voto(ano):
    """
    Analize de permissão do voto no Brasil
    :param ano: ano de nascimento
    :return: se está em situação de NEGADO, OPCIONAL e OBRIGATÓRIO
    """
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos, não é permitido votar!'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos, o voto é opcial!'
    else:
        return f'Com {idade} anos, é orbigatório votar!'


a = int(input('Ano de nascimento: '))
print(voto(a))
