
import logger as log




def get_variant():
    # выдать пользователю список вариантов меню и запросить выбор
    print('''
    Возможные пункты меню:

    1 - рассчитать выражение
    2 - посмотреть лог файл
    3 - выйти из программы
    ''')
    check_input = False
    while not check_input:
        try:
            menu = int(input('Введите пункт меню из предложенных: '))
            log.menu_logger(menu)  # записали в лог
            check_input = True
            if menu > 3 or menu < 1:
                print('Выберите пункт меню от 1 до 3')
                log.error_logger(
                    'Некорректный ввод пункта меню, вне диапазона 1-3')
                check_input = False
        except:
            print('Некорректный ввод, введите число: 1, 2 или 3')
            log.error_logger('Некорректный ввод пункта меню')

    return menu



def get_value():
    print('''
    Обратите внимание:
    1. В рациональных числах 
    - не допускаются "," (запятые) - отделяйте дробную часть "." (точкой),
    например: 2.54-1.05*6.45 и т.п.

    2. Комплексные числа в выражении 
    - должны быть обрамлены скобками (), 
    например: (2+4j)*(1-3j)-(1+8j) и т.п.''')

    # допустимые символы в выражении в списке + сами цифры
    li_char = ['(', ')', '+', '*', '/', '-','.','i','j']
    check_input = False
    while not check_input:
        data = input('\nВведите выражение = ')
        log.input_logger(data)
        check_input = True

        for el in data:
            if not el.isdigit():
                if not el in li_char:
                    print('В выражении недопустимые символы')
                    log.error_logger('В выражении недопустимые символы')
                    check_input = False
                    break

    if "j" in data or "i" in data:  
        type_str = 'c'
    else:
        type_str = 'r'  
    data_input = (type_str, data)

    # по ходу проверки ввода, если что-то пошло не так, записываем ошибку через ф-цию
    # log.error_logger(передаем сюда ошибку)
    
    return data_input  # вернули кортеж



def view_data(data, title):
    print('\nПолучен результат:')
    print(f'{title} = {data}')
    log.res_logger(data)  # показали рез-т и записали в лог


def view_logger(fl):
    log.view_log_logger(fl)  
    with open(fl, 'r', encoding="utf8") as file:
        log_txt = file.read()
    print(log_txt)
    

