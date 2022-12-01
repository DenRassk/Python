# Задание №5
# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

# вычисляем число негафибоначчи
def n_fibon(n):
    if n == 0:
        return 0
    elif n == 1:
        return n_fibon(n - 1) + 1
    else:
        return (n_fibon(n - 2) - n_fibon(n - 1))

# вычисляем число фибоначчи
def fibon(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fibon(n - 1) + fibon(n - 2)



number = int(input('Введите номер последнего члена Фибоначи: '))
if number == 0:
    print('Введите число отличное от нуля')
    exit()

#создаём список чисел негафибоначчи
spis_n_fibon = []
for i in range(number, -1, -1):
    spis_n_fibon.append(n_fibon(i))

#создаём список чисел негафибоначчи
spis_fibon = []
for i in range(1, number + 1):
    spis_fibon.append(fibon(i))

#"склеиваем" и выводим два списка чисел
print(spis_n_fibon + spis_fibon)