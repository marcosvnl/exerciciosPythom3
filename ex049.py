# Refaça o deafio 009, mostrando a tabuaada de um número que o úsuario escolha, só que agora utilizando um laço for.
num = int(input('Digite um número para saber sua TABUADA: '))
for c in range(1, 11):
    print('{} X {} = {}'.format(num, c, num*c))
