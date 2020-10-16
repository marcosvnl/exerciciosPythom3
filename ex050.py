# Desenvolva um programa que leia seis números inteiros e mostre asoma apenas da queles que forem pares.
# Se o número digitado for impar, desconsiderar
soma = 0
cont = 0
for c in range(0, 6):
    num = (int(input('Digite um número: ')))
    if num % 2 == 0:
        soma += num
        cont += 1
print('Foram informados {} números pares e a soma entre eles é {}'.format(cont, soma))
