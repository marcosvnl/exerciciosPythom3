print(10*'~')
print('Sequência de Fibonacci')
print(10*'~')
termo = int(input('Quantos termos você quer var? '))
t1 = 0
t2 = 1
print('{} ¬ {} ¬'.format(t1, t2), end='')
conta = 3
while conta <= termo:
    t3 = t1 + t2
    print(' {} ¬'.format(t3), end='')
    t1 = t2
    t2 = t3
    conta += 1
print(' Fim')