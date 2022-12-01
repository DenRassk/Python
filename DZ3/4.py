# Задание №4 4. Напишите программу, которая будет преобразовывать
#десятичное число в двоичное (встроенными методами пользоваться нельзя).
#Пример:
# 45 -> 101101
#  3 -> 11
#  2 -> 10

def binary(number):
    numberBinary = ''
    while number > 0:
        numberBinary = str(number % 2) + numberBinary
        number = number // 2    
    return numberBinary


number = int(input('Введите натуральное число: '))
if number == 0:
    print ('Число 0 в двоичной системе счисления равно 0')
    exit()
elif number < 0:
    number *= -1 
    print('Число -'+ str(number) + ' в двоичной системе счисления -' + binary(number))
else:
    print('Число '+ str(number) + ' в двоичной системе счисления ' + binary(number))