#Задание №4.
#Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
#Пример:
#Введите текст для кодировки: WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW
#Текст после кодировки: 12W1B12W3B24W1B14W
#Текст после дешифровки: WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW
#Входные и выходные данные хранятся в отдельных текстовых файлах.


def rle (stroka): # кодируем строку по алгоритму RLE
    simvol = ''
    f_rle = ''
    count = 0
    for item in stroka:
        if item == simvol:
            count += 1
        else:
            if simvol:
                f_rle = f_rle + str(count)+simvol
            count = 1
            simvol = item
    return f_rle + str(count)+simvol

def un_rle(stroka):		# раскодируем строку
    f_out = ''
    count = ''
    for item in stroka:
        if item.isdigit():
            count += item
        else:
            f_out += item*int(count)
            count = ''
    return f_out

with open('4_in.txt', 'r') as fin:	# считываем строку
    f_in = fin.read()

if not f_in:
    print ('В файле 4_in.txt нет данных для кодирования')
    exit()

print ('Считали строку из файла 4_in.txt')

f_rle = rle(f_in) # кодируем строку

with open('4_rle.txt', 'w') as frle:	# сохраняем закодированную строку
    frle.write(f_rle)
print ('Закодированная строка сохранена в файл 4_rle.txt')

f_out = un_rle(f_rle)	# раскодируем строку

with open('4_out.txt', 'w') as fout:	# сохраняем раскодированную строку
    fout.write(f_out)
print ('Раскодированная строка сохранена в файл 4_out.txt')