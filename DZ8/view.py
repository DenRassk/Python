# модули визуализации данных (вывод)

# начало работы - запрос имени
def privet():
    print('Вы запустили телефонный справочник')
    iam = input('Представьтесь, пожалуйста: ')
    print('Добрый день, ' + iam)
    
    return iam
    
    
# меню
def menu(iam):
    while True:
        print(iam + ' выберите действие:')
        print('1 - загрузить справочник из файла spr.csv')
        print('2 - посмотреть загруженный справочник')
        print('3 - посмотреть справочник из файла')
        print('4 - добавить нового сотрудника')
        print('5 - изменить данные о сотруднике')
        print('6 - удалить данные о сотруднике')
        print('7 - экспорт справочника в CSV')
        print('8 - экспорт справочника в TXT')
        print('9 - выйти из справочника')
        select = input(iam + ', что Вы выбрали - ')
        if select in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            print(' \n' + '-' * 30 + ' \n')
            break
        else:
            print(iam + ', пожалуйста выберите из предложенных вариантов!')
            print(' \n' + '-' * 30 + ' \n')
    return select
    

# посмотреть загруженный в память справочник
def view_spr_loader(spr):
        print('-' * 30 + '\n Список сотрудников в справочнике:')
        print(*spr, sep = "\n")
        print('-' * 30 + ' \n')


# просмотр справочника из файла
def view_read_spr(sprav):
    print('-' * 30 + '\n Список сотрудников в справочнике:')
    for i,sotrudnik in enumerate(sprav, 0):
        if i != 0:
            print (i, *sotrudnik)
        else:
            print (*sotrudnik)
    print('\n' + '-' * 30 + ' \n')
        
# запрс данных сотрудника
def employee(iam):
    print(iam + ', введите, через пробел, Фамилию, Имя, телефон и должность')
    return input().split()

# запрос номера записи сотрудника
def nom_employee(iam):
    number = ''
    count = 3
    while not number.isdigit():
        if count != 0:
            number = input (f'{iam}, введите номер сотрудника:')
            if not number.isdigit(): print (f'необходимо ввести число, осталось {count} попытки/а')
            count -= 1
        else:
            number = '0'
                          
    return int(number)
    