# Задание №5.
# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.
# многочлен записывается в виде k1*x^5 + k2*x^4 + k3*x^3 + k4*x^2 + k5*x + k6 = 0


#функция составления словаря для многочлена (степень:значение коэффициента)
def slovar(mn):
    mn_slovar ={}
    for el in mn:
        if '*x^' in el:
            tt = el.split('*x^')
            if tt[0] == '':
                mn_slovar[f'{tt[1]}'] = '1'
            else:
                mn_slovar[f'{tt[1]}'] = f'{tt[0]}'        
        elif 'x^' in el:
            tt = el.split('x^')
            if tt[0] == '':
                mn_slovar[f'{tt[1]}'] = '1'
            else:
                mn_slovar[f'{tt[1]}'] = f'{tt[0]}'             
        elif '*x' in el:
            tt = el.split('*x')
            if tt[1] == '': tt[1] = 1 
            if tt[0] == '':
                mn_slovar[f'{tt[1]}'] = '1'
            else:
                mn_slovar[f'{tt[1]}'] = f'{tt[0]}'
        elif 'x' in el:
            tt = el.split('x')
            if tt[1] == '': tt[1] = 1 
            if tt[0] == '':
                mn_slovar[f'{tt[1]}'] = '1'
            else:
                mn_slovar[f'{tt[1]}'] = f'{tt[0]}'
        else:
            tt = (el, '^0')
            mn_slovar[f'{0}'] = f'{tt[0]}'
            
    return mn_slovar


# суммируем словари в один
def sum_mn(sl_m1, sl_m2):
    summa_sl = {}
    if len(sl_m1) >= len(sl_m2):
        one_sl = sl_m1
        two_sl = sl_m2
    else:
        one_sl = sl_m2
        two_sl = sl_m1
    for key, value in one_sl.items():
        if key in two_sl:
            summa_sl[key] = int(one_sl[key]) + int(two_sl[key])
        else:
            summa_sl[key] = int(one_sl[key])
    for key, value in two_sl.items():
        if key not in one_sl:
            summa_sl[key] = int(two_sl[key])
    summa_sl = dict(sorted(summa_sl.items(), key=lambda x: x[0], reverse=True))
    return summa_sl

# считываем 1й многочлен из первого файла и преобразуем в список
with open('mn_1_5.txt') as mn1:
    mn_1 = mn1.read().split()

# считываем второй многочлен из второго файла
with open('mn_2_5.txt') as mn2:
    mn_2 = mn2.read().split()

#(убираем из списка элементы в которых '=', '+' и '0'
print ('Первый многочлен:', ' '.join(mn_1))
print ('Второй многочлен:', ' '.join(mn_2))
mn1 = [el for el in mn_1 if (el != '=' and el != '0' and el != '+')]
mn2 = [el for el in mn_2 if (el != '=' and el != '0' and el != '+')]

#формируем словарь по каждому многочлену (степень:значение коэффициента)
sl_mn1 = slovar(mn1)
sl_mn2 = slovar(mn2)

#считаем сумму многочленов в словарь
summa_mn = sum_mn(sl_mn1, sl_mn2)

# формируем строку - суммарный многочлен
mn_summa = ''
for key, value in summa_mn.items():
    if key == '0' :
        mn_summa = mn_summa + f' {value} '
    elif key == '1' and value == '1':
        mn_summa = mn_summa + ' x ' + '+'
    elif key == '1' and value != '1':
        mn_summa = mn_summa + f' {value}*x ' + '+'
    else:
        if value == 1:
            mn_summa = mn_summa + f' x^{key} ' + '+'
        else: 
            mn_summa = mn_summa + f' {value}*x^{key} ' + '+'
    mn_summa = mn_summa
mn_summa = mn_summa + ' = 0'

# сохраняем в файл
with open('mn_itog_5.txt','w') as mn_i:
    mn_i.write(mn_summa)
print ('Суммарный многочлен: ', mn_summa)
print ('Результат смотрим в файле mn_itog_5.txt')