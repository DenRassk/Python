# тут только запуск и запуск логирования

from controller import main
import logging

# запускаем журналирование
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO, filename="bot_log.log",filemode="w")

# запускаем бота
main()

