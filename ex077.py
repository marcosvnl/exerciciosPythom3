# crie um programa que tenha uma tupla com várias paravras (não usar acentos).
# Depois disso, você deve mostrar, para cada palavras, quais são suas vogais.
palavras = 'amor', 'chamada', 'sistema', 'python',\
           'apoio', 'paralelepipedo', 'pelado', \
           'primitivo', 'pensamento', 'paraquedas',\
           'parquimetro'
for lista in palavras:
    print(f'\nA palavra \33[1;32m{lista.upper()}\33[m tem as vogais ', end='')
    for vogais in lista:
        if vogais.lower() in 'aeiyou':
            print(f'{vogais}', end='')
