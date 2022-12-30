from telegram import ReplyKeyboardRemove, ReplyKeyboardMarkup
from telegram.ext import Updater,ConversationHandler, CommandHandler, MessageHandler, Filters
import random
import logging


candies = 60
step = 15

reply_keyboard = [['/play', '/settings', '/rules', '/hide', '/stop']]
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False, resize_keyboard=True)
reply_keyboard1 = [['/stop']]
markup1 = ReplyKeyboardMarkup(reply_keyboard1, one_time_keyboard=False, resize_keyboard=True)
    
    
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO, filename="bot_log.log",filemode="w")

#TOKEN = token1


def start(update, context):
#    global candies, step
#    candies = 60
    update.message.reply_text(
        f'Привет! Я конфетный бот! У меня есть {candies} конфет и готов поиграть с тобой! \n'
        'Правила игры - /rules \n'
        'Начать игру - /play \n'
        'Настройки - /settings \n'
        'Спрятать кнопки - /hide \n'
        'Надоело или не хочешь играть - /stop',
        reply_markup=markup
    )


def hide_keyb(update, context):
    update.message.reply_text('убрал кнопки', reply_markup=ReplyKeyboardRemove())


def rules(update, context):
    update.message.reply_text(
        'У нас есть конфеты (если 60 мало - в настройках можно задать любое количество). \n'
        'Ходить будем по очереди. Взять можно не более 15 конфет за один ход (тоже можно поменять). \n'
        'Выигрывает, и забирает всё тот, кто забрал последние конфеты. \n'
        'Готов играть - жми /play! Хочешь поменять настройки - /settings \n')


def settings(update, context):
    update.message.reply_text('Через пробел укажи общее количество конфет и сколько максимум можно взять за один раз')
    return 1


def set_settings(update, context):
    global candies, step
    candies, step = map(int, update.message.text.split())
    update.message.reply_text('Пусть будет по твоему! \nВперёд! \nЖми - /play', reply_markup=markup)
    return ConversationHandler.END


def play(update, context):
    update.message.reply_text(f'На столе {candies} конфет. \nНе жадничай, подумай как следует! \nСколько возьмёшь? ',
                              reply_markup=ReplyKeyboardRemove())

    update.message.reply_text('не хочешь играть жми или пиши /stop', reply_markup=markup1)
    return 1


def play_step(update, context):
    global candies,step
    hod = int(update.message.text)
    if hod > step:
        update.message.reply_text(f'Не жадничай! Максимум - {step}!', reply_markup=markup1)
        return 1
    candies -= hod
    if candies == 0:
        update.message.reply_text('Везёт же некоторым... твоя взяла, ПОЗДРАВЛЯЮ!', reply_markup=markup)
        candies = 60
        step = 15
        return ConversationHandler.END
    if candies <= step:
        update.message.reply_text('Я забираю оставшиеся {candies} конфет и выигрываю!!!')
        update.message.reply_text('Хочешь конфетку?', reply_markup=markup)
        candies = 60
        step = 15
        return ConversationHandler.END
    else:
        if candies % (step + 1) == 0:
            hod = random.randint(1, step)
            update.message.reply_text(f'На столе {candies} конфет, пожалуй возьму {hod}', reply_markup=markup1)
            candies -= hod
        else:
            update.message.reply_text(f'На столе {candies} конфет, возьму ка я {candies % (step + 1)}.', reply_markup=markup1)
            candies -= candies % (step + 1)
        if candies <= step:
            update.message.reply_text(f'Вы забираете оставшиеся {candies} конфет и ВЫИГРЫВАЕТЕ! \nКонфеткой не поделитесь?', reply_markup=markup)
            candies = 60
            step = 15
            return ConversationHandler.END
        else:
            update.message.reply_text(f'Осталось {candies} конфет, сколько возьмёте Вы?', reply_markup=markup1)
        


def stop(update, context):
    update.message.reply_text('Понимаю, не у каждого хватит смелости играть с ботом! \n'
                              'Передумаешь - позови набрав /start', reply_markup=ReplyKeyboardRemove())
    return ConversationHandler.END


def main():
    TOKEN = input('Введите свой TOKEN от бота: ')
    updater = Updater(TOKEN)
    settings_hundler = ConversationHandler(
        entry_points=[CommandHandler('settings', settings)],
        states={1: [MessageHandler(Filters.text & ~Filters.command, set_settings)]},
                fallbacks=[CommandHandler('stop', stop)]
    )

    play_hundler = ConversationHandler(
        entry_points=[CommandHandler('play', play)],
        states={1: [MessageHandler(Filters.text & ~Filters.command, play_step)]},
                fallbacks=[CommandHandler('stop', stop)])

    updater.dispatcher.add_handler(CommandHandler("start", start))
    updater.dispatcher.add_handler(CommandHandler("rules", rules))
    updater.dispatcher.add_handler(CommandHandler("stop", stop))
    updater.dispatcher.add_handler(CommandHandler("hide", hide_keyb))
    updater.dispatcher.add_handler(settings_hundler)
    updater.dispatcher.add_handler(play_hundler)


    updater.start_polling()
    print('bot starting...')
    updater.idle()

main()