número = soma = conta = 0
while True:
    número = int(input('Digite uma número [digite 999 p/ para]: '))
    conta += 1
    if número == 999:
        break
    soma = soma + número
print(f'Foram digitados {conta - 1} números e a soma entre os números selecionados é {soma}')
