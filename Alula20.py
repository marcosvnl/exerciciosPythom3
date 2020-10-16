def soma(a, b):
    s = a + b
    print(s)


soma(5, 4)
# a = 5
# b = 4
# s = a + b
# print(s)
soma(3, 5)
# a = 3
# b = 5
# s = a + b
# print(s)
soma(2, 8)


# a = 2
# b = 8
# s = a + b
# print(s)
def contador(*num):
    tam = len(num)
    print(f'Recebi os valores {num} e ao total são {tam} números')


contador(3, 5, 4, 9, 6, 7)
contador(2, 5, 7)