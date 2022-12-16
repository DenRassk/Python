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
        print('2 - посмотреть справочник')
        print('3 - экспорт справочника в CSV')
        print('4 - экспорт справочника в TXT')
        print('5 - выйти из справочника')
        select = input(iam + ', что Вы выбрали - ')
        if select == '1' or select == '2' or select == '3' or select == '4' or select == '5':
            print(' \n' + '-' * 30 + ' \n')
            break
        else:
            print(iam + ', пожалуйста выберите из предложенных вариантов!')
            print(' \n' + '-' * 30 + ' \n')
    return select
    

# посмотреть справочник
def view_spr(spr):
        print('-' * 30 + ' \nТелефонный справочник:')
        print(*spr, sep = "\n")
        print('-' * 30 + ' \n')
 
    