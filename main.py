#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import importlib

# карта заданий: номер -> (имя модуля, описание)
TASKS = {
    '0': ('00_distance',        'Расстояния между городами'),
    '1': ('01_circle',          'Площадь круга и проверка точек'),
    '2': ('02_operations',      'Расстановка арифметических знаков'),
    '3': ('03_favorite_movies', 'Срезы строки фильмов'),
    '4': ('04_my_family',       'Семья и рост'),
    '5': ('05_zoo',             'Операции со списком животных зоопарка'),
    '6': ('06_songs_list',      'Время звучания песен Depeche Mode'),
    '7': ('07_secret',          'Расшифровка секретного сообщения'),
    '8': ('08_garden',          'Множества цветов (сад и луг)'),
    '9': ('09_shopping',        'Минимальные цены в магазинах'),
    '10': ('10_store',          'Складские запасы и стоимость'),
}


def run_task(module_name):
    """Импортирует модуль и запускает его функцию run()."""
    module = importlib.import_module(module_name)
    importlib.reload(module)
    module.run()


def run_all():
    """Запускает все задания по порядку."""
    for num, (module_name, title) in TASKS.items():
        print(f'\n>>> ЗАДАНИЕ {num}: {title.upper()} <<<\n')
        run_task(module_name)


def print_menu():
    print('\n=== МЕНЮ ЛАБОРАТОРНОЙ РАБОТЫ №1 ===')
    for num, (_, title) in TASKS.items():
        print(f'  {num:>2} — {title}')
    print('   a — выполнить все задания')
    print('   q — выход')


def main():
    while True:
        print_menu()
        choice = input('Ваш выбор: ').strip().lower()

        if choice == 'q':
            print('Выход.')
            break
        elif choice == 'a':
            run_all()
        elif choice in TASKS:
            module_name, title = TASKS[choice]
            print(f'\n>>> ЗАДАНИЕ {choice}: {title.upper()} <<<\n')
            run_task(module_name)
        else:
            print('Некорректный ввод, попробуйте снова.')


if __name__ == '__main__':
    main()