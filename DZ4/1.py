#Задание №1 Вычислить число c заданной точностью d
#Пример:
#- при $d = 0.001, π = 3.142.$    $10^{-1} ≤ d ≤10^{-10}$
# !!!! округление происходит по правилам математики а не отбрасыванием лишнего!!!

import math 
string =  input('Введите точность округления (например 0.0001) :')
d = len(string)-2

if int(math.pi * 10**(d+1)-int(math.pi*10**d)*10) >= 5:
    print((int(math.pi*10**d)+1)/(10**d))
else: print((int(math.pi*10**d))/(10**d))
