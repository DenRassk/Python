#Реализуйте алгоритм перемешивания списка
#(shuffle использовать нельзя, другие методы из библиотеки random - можно).

import random

stroka = input('Введите любую строку: ')
if stroka.strip() == "":
    print ('Вы ввели пустую строку! Попробуйте ещё раз')
else:
    stroka_spis = list(stroka)
    for i in range(0, len(stroka)-1):
        r = random.randint(0,len(stroka)-1)
        j = stroka_spis[i]
        stroka_spis[i] = stroka_spis[r]
        stroka_spis[r] = j
        i +=1
    
    print ('Перепутанная строка: ' + "".join(stroka_spis))