import csv
import view


# считать справочник из файла spr.csv
def load_spr():
    spr = []
    with open("spr.csv", encoding='utf-8') as r_file: 
        reader_object = csv.reader(r_file, delimiter = ",")
        count = 0
        for row in reader_object:
            if row != ['Фамилия', 'Имя', 'телефон', 'должность']:
                spr.append(row)
            count += 1
    return spr


# экспорт справочника в csv
def export_csv(spr, iam):
    stop = 3
    while True:
        file = input(f'{iam}, введите имя файла ')
        if file != '':
            with open(file, mode="w", encoding='utf-16') as w_file:
                file_writer = csv.writer(w_file, delimiter = ",", lineterminator="\r")
                file_writer.writerow(['Фамилия', 'Имя', 'телефон', 'должность'])
                for row in spr:
                    file_writer.writerow(row)
            print(f'{iam}, телефонный справочник записан в файл {file} \n')
            break
        else:
            print(f'{iam}, Вы ни чего не ввели')
            print(f'у Вас ещё {stop} попытки \n')
            stop -= 1
            if stop == 0: break
            

# экспорт справочника в txt
def export_txt(spr, iam):
    stop = 3
    while True:
        file = input(f'{iam}, введите имя файла ')
        if file != '':
            with open(file, 'w', encoding='utf-8') as fout:
                fout.write('Фамилия' + ',' + 'Имя' + ',' + 'телефон' + ',' + 'должность' + '\n')
                for row in spr:
                    fout.write(','.join(row)+'\n')
            print(f'{iam}, телефонный справочник записан в файл {file} \n')
            break
        else:
            print(f'{iam}, Вы ни чего не ввели')
            print(f'у Вас ещё {stop} попытки \n')
            stop -= 1
            if stop == 0: break


def read_spr_file():
    with open('spr.csv', 'r', encoding = 'utf-8') as file:
        reader = csv.reader(file, delimiter = ',')
        return list(reader)


def add_employee(data):
    with open('spr.csv',mode = 'a', encoding='utf-8', newline = '') as file:
        writer = csv.writer(file, delimiter = ",", lineterminator="\r")
        writer.writerow(data)
    print('Данные о новом сотруднике добавлены в справочник!')
    print(' \n' + '-' * 30 + ' \n')


# вносим изменение записи в справочник
def change_employee(number,data):
    with open('spr.csv', 'r', encoding='utf-8',newline = '') as file:
        reader = list(csv.reader(file, delimiter = ','))
        print (len(reader))
    if len(reader) >= number+1 :
        reader[number] = data
        with open('spr.csv',mode = 'w', encoding='utf-8', newline = '') as file:
            writer = csv.writer(file, delimiter = ",")
            for i in reader:
                writer.writerow(i)
        print('Данные о сотруднике изменены!')
    else:
        print (f'Сотрудника с номером {str(number)} нет в справочнике!')
        
    print(' \n' + '-' * 30 + ' \n')

# удаляем запись
def delete_employee(number):
    with open('spr.csv', 'r', encoding='utf-8',newline = '') as file:
        reader = list(csv.reader(file, delimiter = ','))
    if len(reader) >= number+1 :
        del reader[number]
        with open('spr.csv',mode = 'w', encoding='utf-8', newline = '') as file:
            writer = csv.writer(file, delimiter = ",")
            for i in reader:
                writer.writerow(i)
        print('Данные сотрудника удалены!')
    else:
        print (f'Сотрудника с номером {str(number)} нет в справочнике!')
        
    print(' \n' + '-' * 30 + ' \n')               
