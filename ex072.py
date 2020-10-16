# Crie um preograma que tenha uma tupla totalmente preenchida com uma contaguem por extenso, de zero até vinte.
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
números = 'Zero', 'Um', 'Dois', 'Três', 'Quatro',\
          'Cinco', 'Seis', 'Sete', 'Oito', 'Nove',\
          'Dez', 'Onze', 'Deoze', 'Treze', 'Catorze',\
          'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte'
while True:
    escolha = int(input('Digite um número de 0 a 20: '))
    if 0 <= escolha <= 20:
        break
    print('ERRO:', end=' ')
print(f'Você digitou o número {escolha}')
print(f'Escrito por extenso {números[escolha]}')
