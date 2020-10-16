#022: Crie um programa que leia o nome completo de
#uma pessoa e mostre: - O nome com todas as letras
#maiúsculas e minúsculas. - Quantas letras ao todo
#(sem considerar espaços). - Quantas letras tem o
#primeiro nome.
nome = str(input('Digite seu nome completo: ')).strip()
print(str('Analizando seu nome:'))
print('Apenas com letras máiusculas; {}'.format(nome.upper()))
print('Apenas com letras minusculas; {}'.format(nome.lower()))
print('Seu nome completo tem {} letras'.format(len(nome) - nome.count(' '))) # contar qtd de letras - qtd de espaços
#print('Seu primeiro nome tem {} letras'.format(nome.find(' '))) (uma das opcões)
separa = nome.split()
print('Seu primeiro nome é {} e tem {} letras'.format(separa[0], len(separa[0])))
