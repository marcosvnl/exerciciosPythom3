# Exercício Python 092: Crie um programa que leia nome,
# ano de nascimento e carteira de trabalho e cadastre-o (com idade)
# em um dicionário. Se por acaso a CTPS for diferente de ZERO,
# o dicionário receberá também o ano de contratação e o salário.
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
from datetime import date
atual = date.today().year
dados = dict()
dados['nome'] = str(input('Nome: '))
dados['ano'] = int(input('Ano de nascimento: '))
dados['CTPS'] = int(input('CTPS [digite 0 se não obiter ctps]: '))
dados['idade'] = atual - dados['ano']
if dados['CTPS'] != 0:
    dados['ano_in'] = int(input('Ano de inicio na empresa: '))
    dados['salario'] = float(input('salário:'))
    dados['aposenta'] = dados['idade'] + 30
print('-='*30)
for k, v in dados.items():
    print(f'- {k}, {v}')

