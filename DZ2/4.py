# 4. Задайте список из N элементов, заполненных числами
# из промежутка [-N, N]. Найдите произведение элементов
# на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.

poz1 = poz2 = err = 0

number = int(input('Введите целое число больше нуля: '))
if number < 0:
    print ('Вы ввели отрицательное число! \nПопробуйте ещё раз!')
elif number == 0:
    print ('Вы ввели ноль! \nПопробуйте ещё раз!')
else:
    massiv = []
    for i in range (-number, number +1):
        massiv.append(i)
    print ('Числовая шкала ', massiv)

#считывае индексы из файла
with open("file.txt", "r") as file:
    str1 = file.readline()
    str2 = file.readline()

print ('Из файла считано следующее:')

# проверяем первое число
print ('номер первой позиции - ' + str1[0])

if str1[0].isdigit():
    poz1 = int(str1[0])
    if (poz1 > number*2+1 ):
        print ('Внимание! На числовой шкале НЕТ позиции номер ' + str1[0])
        err = 1
else:
    print ('Внимание! Это не число!')
    err = 1

# проверяем второе число
print ('номер второй позиции - ' + str2)
if str2[0].isdigit():
    poz2 = int(str2[0])
    if (poz2 > number*2 ):
        print ('Внимание! На числовой шкале НЕТ позиции номер ' + str2[0])
        err = 1
else:
    print ('Внимание! Это не число!')
    err = 1

if err == 1:
    print ('Устраните ошибки и повторите расчёт')
else:
    print('Произведение чисел на позициях с номерами ' + str1[0] + ' и ' + str2[0] + ' равна:')
    print(massiv[poz1-1],' * ',massiv[poz2-1],' = ', massiv[poz1-1]*massiv[poz2-1])
