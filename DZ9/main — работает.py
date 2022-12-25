
from telegram import ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, ConversationHandler, MessageHandler, Filters 
import logging
import csv


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO, filename="bot_log.log",filemode="w")

def start(update, context):
    context.bot.send_message(chat_id = update.effective_chat.id,
                             text = '''Добрый день. Я Бот - телефонный справочник!
Наберите:
 /view - для просмотра всего српавочника
 /surname - для поиска по Фамилии
 /add_user - для добавления абонента
 /del_user - для удаления абонента
 /edit_user - для редактирования записи''')



# запрос фамилии для поиска
def surname(update, context):
    update.message.reply_text(
        'Для поиска в справочнике напишите фамилию: \n'
        'для отказа от поиска наберите /stop')
    return 1


# поиск по фамилии
def find(update, context):
    surname = update.message.text
    sprav = read_spr_file()
    for row in sprav:
        if row[0] == surname:
            context.bot.send_message(chat_id = update.effective_chat.id,
                             text = ', '.join(row))        
    return ConversationHandler.END


# добавление записи в справочник - запрос данных
def add_user(update, context):
    update.message.reply_text(
        'Для добавления записи в справочник напишите через запятую\n'
        'Фамилию,имя,номер телефона,должность: \n'
        'для отказа от добавления записи наберите /stop')    
    
    return 1


# добавление записи в справочник - собственно добавляем данные
def add_row(update, context):
    with open('spr.csv',mode = 'a', encoding='utf-8', newline = '') as file:
        writer = csv.writer(file, lineterminator="\r")
        writer.writerow(update.message.text.split(sep=','))    
    update.message.reply_text('Данные о новом абоненте добавлены в справочник.')
    
    return ConversationHandler.END


# удаление записи из справочника - запрос номера записи
def del_user(update, context):
    update.message.reply_text(
        'Для удаления записи из справочника  введите номер записи\n'
        '(для отказа от удаления записи наберите /stop)')    
    
    return 1


# удаление записи из справочника - удаление записи
def del_row(update, context):
    with open('spr.csv', 'r', encoding='utf-8',newline = '') as file:
        reader = list(csv.reader(file, delimiter = ','))
    if len(reader) >= int(update.message.text)+1 :
        del reader[int(update.message.text)]
        with open('spr.csv',mode = 'w', encoding='utf-8', newline = '') as file:
            writer = csv.writer(file, delimiter = ",")
            for i in reader:
                writer.writerow(i)
        update.message.reply_text('Данные о абоненте удалены из справочника.')
    else:
        update.message.reply_text(f'Абонента с номером {update.message.text} нет в справочнике!')
 
    return ConversationHandler.END


# редактирование записи в справочнике - запрос данных
def edit_user1(update, context):
    update.message.reply_text(
        'Для изменения записи в справочнике введите\n'
        'номер записи: \n'
        '(для отказа от добавления записи наберите /stop)')    
    
    return 1

# редактирование записи в справочнике - запрос данных
def edit_user2(update, context):
    global number
    number = int(update.message.text)
    update.message.reply_text(
        'Напишите, через запятую\n'
        'Фамилия,имя,номер телефона,должность: \n'
        '(для отказа от добавления записи наберите /stop)')    
    
    return 2

# редактирование записи в справочнике - собственно добавляем данные
def edit_row(update, context):
    global number    
    with open('spr.csv', 'r', encoding='utf-8',newline = '') as file:
        reader = list(csv.reader(file))
    if len(reader) >= number+1 :
        reader[number] = update.message.text.split(sep=',')
        with open('spr.csv',mode = 'w', encoding='utf-8', newline = '') as file:
            writer = csv.writer(file)
            for i in reader:
                writer.writerow(i)
        update.message.reply_text('Данные о абоненте изменены!')
    else:
        update.message.reply_text(f'Абонента с номером {str(number)} нет в справочнике!')    
    
    return ConversationHandler.END



# просмотр справочника
def view(update, context):
    text_ = view_read_spr(read_spr_file())
    context.bot.send_message(chat_id = update.effective_chat.id,
                             text = text_)
    
    
# загружаем справочник из файла
def read_spr_file():
    with open('spr.csv', 'r', encoding = 'utf-8') as file:
        reader = csv.reader(file, delimiter = ',')
        return list(reader)


# формируем список абонентов
def view_read_spr(sprav):
    text = 'Список сотрудников в справочнике: \n'
    for i,sotrudnik in enumerate(sprav, 0):
        if i != 0:
            text += str(i)+'. ' + ', '.join(sotrudnik) + '\n'
        else:
            text += ', '.join(sotrudnik)+'\n'
    return text


# остановка обработки
def stop(update, context):
    update.message.reply_text("До свидания")
    return ConversationHandler.END

    
# запускаем бота
def main():
    TOKEN = '5439736558:AAH-lgsDXKfKm2fkFwu4zhyE4J40CiEQHU4'
    updater = Updater(token = TOKEN)
    dispatcher = updater.dispatcher
# описываем поиск по фамилии
    find_surname = ConversationHandler(entry_points=[CommandHandler('surname', surname)],
                                       states={1: [MessageHandler(Filters.text & ~Filters.command, find)]},
               fallbacks=[CommandHandler('stop', stop)])
# описываем добавление записи
    add_us = ConversationHandler(entry_points=[CommandHandler('add_user', add_user)],
                                       states={1: [MessageHandler(Filters.text & ~Filters.command, add_row)]},
               fallbacks=[CommandHandler('stop', stop)])
# описываем изменение записи
    edit_us = ConversationHandler(entry_points=[CommandHandler('edit_user', edit_user1)],
                                       states={1: [MessageHandler(Filters.text & ~Filters.command, edit_user2)],
                                               2: [MessageHandler(Filters.text & ~Filters.command, edit_row)]},
               fallbacks=[CommandHandler('stop', stop)])
# описываем удаленние записи
    del_us = ConversationHandler(entry_points=[CommandHandler('del_user', del_user)],
                                       states={1: [MessageHandler(Filters.text & ~Filters.command, del_row)]},
               fallbacks=[CommandHandler('stop', stop)])   
# возможные команды боту    
    dispatcher.add_handler(CommandHandler('start', start))		# запуск бота
    dispatcher.add_handler(CommandHandler('view', view))		# просмотр справочника
    dispatcher.add_handler(find_surname)	# поиск по фамилии
    dispatcher.add_handler(add_us)	# поиск по фамилии
    dispatcher.add_handler(edit_us)	# поиск по фамилии
    dispatcher.add_handler(del_us)	# поиск по фамилии    
    dispatcher.add_handler(CommandHandler('help', help))	#

    updater.start_polling()
    print('bot start')
    
    updater.idle()

    

main()

