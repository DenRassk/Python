import view
import model


# запуск справочника
def start_spav():
    iam = ''
    spr = []
    iam = view.privet()
    while True:
        select = view.menu(iam)
        if select == '9': # выход из программы
            break
        elif select == '1': # считать справочник из файла
            spr = model.load_spr()
            print('Справочник успешно считан из файла \n')
        elif select == '2': # посмотреть загруженный справочник
            if spr != []:
                view.view_spr_loader(spr)
            else:
                print(f'{iam}, сначало необходимо загрузить справочник \n')
        elif select == '3': # посмотреть справочник в файле
            sprav = model.read_spr_file()
            view.view_read_spr(sprav)
        elif select == '4': # добавить нового сотрудника
            data = view.employee(iam)
            model.add_employee(data)
        elif select == '5': # изменить запись
            sprav = model.read_spr_file()
            view.view_read_spr(sprav)
            number = view.nom_employee(iam)
            if number != 0:
                data = view.employee(iam)
                model.change_employee(number,data)
            else:
                print(f'{iam}, необходимо ввести правильный номер сотрудника \n')
                            
        elif select == '6': # удалить запись
            sprav = model.read_spr_file()
            view.view_read_spr(sprav)
            number = view.nom_employee(iam)
            if number != 0:
                model.delete_employee(number)
            else:
                print(f'{iam}, необходимо ввести правильный номер сотрудника \n')

        elif select == '7': # сохранить загруженный справочник в csv
            spr = model.load_spr()
            model.export_csv(spr, iam)
            
        elif select == '8': # сохранить загруженный справочник в txt
            spr = model.load_spr()
            model.export_txt(spr, iam)
            
        else:
            continue




