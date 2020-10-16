# 065 Crie um progrma que leia varios números inteiros pelo teclado. No final da execução, mostre a média
# entre todos os valores e o maior e o menor número digitado. programa deve perguntar ao usúario se ele
# quer ou não continuar a digitar valores.
maior = 0
menor = 0
mais = ''
soma = 0
conta = 0
media = 0
while mais != 'N':
    numero = int(input('Digite um número: '))
    soma += numero
    conta += 1
    if conta == 1:
        maior = numero
        menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    mais = str(input('Quer contunuar a digitar números[S/N]: ')).strip().upper()[0]
media = soma / conta
print(soma)
print('Foram digirados {} números'.format(conta))
print('A media entres os números digitados é {:.2f}'.format(media))
print('O número maior é {}'.format(maior))
print('E o menor é {}.'.format(menor))
