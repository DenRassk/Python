from view import privet
from view import menu
from view import view_spr
from model import load_spr
from model import export_csv
from model import export_txt


# запуск справочника
def start_spav():
    iam = ''
    spr = []
    iam = privet()
    while True:
        select = menu(iam)
        if select == '5':
            break
        elif select == '1':
            spr = load_spr()
            print('Справочник успешно считан из файла \n')
        elif select == '2':
            if spr != []:
                view_spr(spr)
            else:
                print(f'{iam}, сначало необходимо загрузить справочник \n')
        elif select == '3':
            if spr != []:
                export_csv(spr, iam)
            else:
                print(f'{iam}, сначало необходимо загрузить справочник \n')
        elif select == '4':
            if spr != []:
                export_txt(spr, iam)
            else:
                print(f'{iam}, сначало необходимо загрузить справочник \n')
        else:
            continue




