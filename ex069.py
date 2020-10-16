# Crie uma programa que leia a idade e o sexo de varias pessoas. A cada pessoa cadastrada, o programa deverá
# perguntar se o úsuario quer ou não continuar. No final, mostre:
# quantas pessoas tem mais de 18 anos
# quantos homens foram cadastrados
# quantas mulheres tem menos de 20 anos.
homem = mulher = menor18 = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: ')).upper().strip()[0]
        if idade < 18:
            menor18 += 1
        if sexo == 'M':
            homem += 1
        if sexo == 'F' and idade < 20:
            mulher += 1
    continua = ' '
    while continua not in 'SN':
        continua = str(input('Quer continuar a cadastrar pessoas? [S/N]')).upper().strip()[0]
    if continua == 'N':
        break
print(f'Foram cadastrados {menor18} pessoas com menos de 18 anos')
print(f'Foram cadastrados {homem} do sexo Masculino')
print(f'Foram cadastradas {mulher} pesssoas do sexo feminino com menos de 20 anos   ')