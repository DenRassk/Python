# Задание №3
# Создайте программу для игры в "Крестики-нолики"

import random

# выводим игровое поле
def ig_pole(mesto,znak):
    if mesto != 0 and znak != '0':
        pole[mesto] = znak
    print ('Игровое поле:')
    print (' ' + pole[1] + ' | ' + pole[2] + ' | '+ pole[3])
    print (' --+---+--')
    print (' ' + pole[4] + ' | ' + pole[5] + ' | '+ pole[6])
    print (' --+---+--')
    print (' ' + pole[7] + ' | ' + pole[8] + ' | '+ pole[9])

# проверяем - выиграл кто-то или как?
def result():
    kto = ''
    for i in pobeda:
        if pole[i[0]] == "X" and pole[i[1]] == "X" and pole[i[2]] == "X":
            kto = "X"
        if pole[i[0]] == "O" and pole[i[1]] == "O" and pole[i[2]] == "O":
            kto = "O"
        if kto != '': continue
    return kto


# создаём и показываем игровое поле 
pole = ['0','1','2','3','4','5','6','7','8','9']
ig_pole(0,'O')
# список вариантов когда выигрываем
pobeda = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]

# представление игроков и жеребьёвка
igrok_1 = input('Введите имя первого игрока: ')
igrok_2 = input('Введите имя второго игрока: ')
if random.randint(1,2) == 1:
    xod_1 = igrok_1
    xod_2 = igrok_2
else:
    xod_1 = igrok_2
    xod_2 = igrok_1

print (xod_1 + ' начинает игру и играет - Х')
print (xod_2 + ' играет - O')

# собственно играем
count_xod = 0
znak = 'X'
while count_xod < 9:
    if znak == 'X':
        mesto = int(input(xod_1+' - куда будем ставить Х ?'))
        ig_pole(mesto, znak)
    else:
        mesto = int(input(xod_2+' - куда будем ставить O ?'))
        ig_pole(mesto, znak)
    kto = result() # кто же победил?
    if kto != '':
        count_xod = 10
    count_xod += 1
    if znak == 'X' and count_xod <10:
        znak = 'O'
    elif znak == 'O' and count_xod <10:
        znak = 'X'    
    

if kto == 'X':
    print('УРА!!! Поздравляем ' + xod_1 + ' победитель!')
elif kto == 'O':
    print('УРА!!! Поздравляем ' + xod_2 + ' победитель!')
else:
    print('Поздравляем ' + xod_1+ ' и ' + xod_2 + ' с боевой ничьёй!')