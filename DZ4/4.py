# Задание № 4.
# Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k.
# Пример:
# k=2 => 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

# !!!!для упрощения алгоритма коэффициенты многочлена формируем больше нуля!!!

import random

k = input('Задайте степень многочлена (введите натуральное число): ')
if k.isdigit:
    k = int(k)
else:
    print('Необходимо ввести натуральное число')
    exit()
    
massiv = []
mnogochlen = ''
for i in range (0, k+1, 1):
    massiv.append(random.randint(0,100))
    if massiv[i] != 0 and i == k:
        mnogochlen = mnogochlen + ' + ' + str(massiv[i]) 
    elif (i !=k and i != k-1 and i != 0) and massiv[i] != 0:
        if mnogochlen != '':
            mnogochlen = mnogochlen + ' + ' + str(massiv[i]) + '*x**'+str(k-i)
        else:
            mnogochlen = str(massiv[i]) + '*x**'+str(k-i)
    elif massiv[i] != 0 and i == k-1:
        mnogochlen = mnogochlen + ' + ' + str(massiv[i]) + '*x'
    elif massiv[i] != 0 and i == 0:
        mnogochlen = str(massiv[i]) + '*x**'+str(k)

mnogochlen =  mnogochlen + ' = 0'        

with open('dz4.txt', 'w') as f:
    f.write('Заданая степень многочлена - ' + str(k) + ' \n Коэффициенты многочлена - ' + ', '.join(map(str, massiv)) + '\n')
with open('dz4.txt', 'a') as f:
    f.write(mnogochlen)

