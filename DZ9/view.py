from telegram import ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, ConversationHandler, MessageHandler, Filters
from model import read_spr_file, view_read_spr


# сообщение при команде /start
def start(update, context):
    context.bot.send_message(chat_id = update.effective_chat.id,
                             text = '''Добрый день. Я Бот - телефонный справочник!
Наберите:
 /view - для просмотра всего српавочника
 /surname - для поиска по Фамилии
 /add_user - для добавления абонента
 /del_user - для удаления абонента
 /edit_user - для редактирования записи''')


# просмотр справочника
def view(update, context):
    text_ = view_read_spr(read_spr_file())
    context.bot.send_message(chat_id = update.effective_chat.id,
                             text = text_)


# запрос фамилии для поиска
def surname(update, context):
    update.message.reply_text(
        'Для поиска в справочнике напишите фамилию: \n'
        'для отказа от поиска наберите /stop')
    return 1


# добавление записи в справочник - запрос данных
def add_user(update, context):
    update.message.reply_text(
        'Для добавления записи в справочник напишите через запятую\n'
        'Фамилию,имя,номер телефона,должность: \n'
        'для отказа от добавления записи наберите /stop')    
    
    return 1



# удаление записи из справочника - запрос номера записи
def del_user(update, context):
    update.message.reply_text(
        'Для удаления записи из справочника  введите номер записи\n'
        '(для отказа от удаления записи наберите /stop)')    
    
    return 1

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