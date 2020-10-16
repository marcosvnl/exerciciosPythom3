# 053 - Crie um programa que leia uma frase qualquer inteira e diga se ela é um políndromo desconsiderando os espaços.
frase = str(input('Digite uma frase para saber se ela é políndromo\nFrase: ')).strip().upper()
separa = frase.split()
esp = ''.join(separa)
inverso = ''
for letras in range(len(esp) - 1, -1, -1):
    inverso = inverso + esp[letras]
print('Normal: {}'.format(esp))
print('Inverso: {}'.format(inverso))
if inverso == esp:
    print('A frase:\n- {}\n É um POLÍNDROMO!'.format(frase))
else:
    print('A frase\n{}\nNão é um POLÍNDROMO!'.format(frase))
