# 064 Crie um programa que leia varios números inteiros pelo teclado. o programa só vai parar quando o usúario digitar
# o valor 999, que é a condição de parada. no final, mostre quantos números foram gigitados e qual foi a soma
# entre eles.(descontando o flag).
conta = 0
soma = 0
flag = int(999)
num = 0
print('\33[4;35m=|Calculadora Maluca|=\33[m')
print('Digite quantos números quiser')
print('Vou falar quantoes números você digitou e a soma entre totos eles!')
print('Digite 999 quando quiser parar ok!')
print(25 * '\33[1;34m=-=\33[m')
while num != flag:
    num = int(input('Digite o {}° número inteiro: '.format(conta + 1)))
    soma += num
    conta += 1
    if num == flag:
        soma -= flag
        conta -= 1
print('Você digitou {} números!'.format(conta))
print('E a soma entre eles é {}!'.format(soma))
