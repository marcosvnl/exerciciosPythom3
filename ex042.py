# 042 Refaça o Desafio 035 dos triângulos acrescentando o resurso de mostrar que tipo de triângulo será formado.
# Equilatero: Todops os lados iguais
# Isómetrico: Dois lados iguais
# Escaleno: Todos os lados diferentes
bas = float(input('Digite o valor da base do TRIÂGULO: '))
alt = float(input('Digite o valor da altura do TRIÂNGULO: '))
com = float(input('Digite o valor do comprimento do TRIÂGULO: '))
if bas <= alt + com and alt <= bas + com and com <= bas + alt:
    print('É possivel formar um triângulo ', end='')
    if bas == alt == com:
        print('EQUILATERO!')
    elif bas != alt != com != bas:
        print('ESCALENO')
    else:
        print('ISÓMETRICO')
else:
    print('Com {}, {}, {} não é possival formar um triangulo!'.format(bas, alt, com))
