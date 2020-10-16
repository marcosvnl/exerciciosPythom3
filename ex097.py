# Exercício Python 097: Faça um programa que tenha uma função chamada escreva(),
# que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
#
# Ex:
# escreva('Olá, Mundo!')
# Saída:
# ~~~~~~~~~
# Olá, Mundo!
# ~~~~~~~~~

def escreva(msg):
    line = len(msg) + 4
    print('~' * line)
    print(f'  {msg}')
    print('~' * line)


escreva('Olá, Mundo!')
escreva('Oi!')
escreva('Marcos Vinicius Nunes de Lima')
