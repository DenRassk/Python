# Задание №3 Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением
# дробной части элементов.

# Пример:

# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random
from decimal import Decimal

number = int(input('Введите количество элементов в списке больше двух: '))
if number == 0 or number == 1:
    print('Количество элементов в списке не может быть меньше двух')
    exit()

# заполняем список
spisok = []
for i in range(1,number+1):
    spisok.append(round((random.random()*10),2)) 
    i += 1
print('Полученный список: ', spisok)

n_min = round((spisok[0]-(spisok[0]//1)),2)
n_max = round((spisok[1]-(spisok[1]//1)),2)
if n_min > n_max:
    vrem = n_min
    n_min = n_max
    n_max = vrem

print(n_max)
print(n_min)

if number > 2:
    for i in range(2,number-1,1):
        vrem = round((spisok[i]-(spisok[i]//1)),2)
        if  vrem > n_max:
            n_max = vrem
        elif n_min > vrem:
            n_min = vrem

print ('Максимальная дробная часть равна ', n_max)
print ('Минимальная дробная часть равна ', n_min)
print ('Разница между ними равна ',round(n_max-n_min,2))


