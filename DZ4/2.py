# Задание №2
# Задайте натуральное число N.
# Напишите программу, которая составит список простых множителей числа N.

n = input('Введите натуральное число: ')
if n.isdigit() == False:
    print('Введите натуральное число!')
else:
    number = int(n)
    mnogitels = []

    delitel = 2
    while delitel <= number:
        if number % delitel == 0:
            number = number/delitel
            mnogitels.append(delitel)
        else:
            delitel += 1

    print('Число ', n, ' = ', ' * '.join(map(str, mnogitels)))