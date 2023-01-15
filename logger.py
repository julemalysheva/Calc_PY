from datetime import datetime as dt


# from time import time


# записываем в лог выбранный вариант меню с указанием даты/времени
def menu_logger(data):
    with open('log.txt', 'a', encoding="utf8") as file:
        file.write('{} Выбран пункт меню {}\n'
                   .format(dt.now().strftime('%d.%m.%Y-%H:%M'), data))


# записываем в лог введенную строку для расчета с указанием даты/времени
def input_logger(data):
    with open('log.txt', 'a', encoding="utf8") as file:
        file.write('{} Введена строка {}\n'
                   .format(dt.now().strftime('%d.%m.%Y-%H:%M'), data))


# записываем в лог ошибку с указанием даты/времени - аргумент data будет передаваться на стороне view
# на этапе обработки - здесь  просто фиксация
def error_logger(data):
    with open('log.txt', 'a', encoding="utf8") as file:
        file.write('{} Зафиксирована ошибка {}\n'  # по хорошему как-то обозначить, какая
                   .format(dt.now().strftime('%d.%m.%Y-%H:%M'), data))


# записываем в лог выдачу результата - аргумент data будет передаваться на стороне view
def res_logger(data):
    with open('log.txt', 'a', encoding="utf8") as file:
        file.write('{} Получен результат вычисления {}\n'
                   .format(dt.now().strftime('%d.%m.%Y-%H:%M'), data))


# записываем в лог показ файла лог - сама выдача будет описана на стороне view
# здесь фиксируем это событие
def view_log_logger(data):
    with open('log.txt', 'a', encoding="utf8") as file:
        file.write('{} Выдан файл лога по запросу {}\n'
                   .format(dt.now().strftime('%d.%m.%Y-%H:%M'), data))
