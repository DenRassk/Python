import csv


# считать справочник из файла spr.csv
def load_spr():
    spr = []
    with open("spr.csv", encoding='utf-8') as r_file: 
        reader_object = csv.reader(r_file, delimiter = ",")
        count = 0
        for row in reader_object:
            if row != ['Фамилия', 'Имя', 'Телефон', 'Описание']:
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
                file_writer.writerow(['Фамилия', 'Имя', 'Телефон', 'Описание'])
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
                fout.write('Фамилия' + ',' + 'Имя' + ',' + 'Телефон' + ',' + 'Описание' + '\n')
                for row in spr:
                    fout.write(','.join(row)+'\n')
            print(f'{iam}, телефонный справочник записан в файл {file} \n')
            break
        else:
            print(f'{iam}, Вы ни чего не ввели')
            print(f'у Вас ещё {stop} попытки \n')
            stop -= 1
            if stop == 0: break
