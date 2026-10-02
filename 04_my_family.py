#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def run():
    # моя семья
    my_family = ['Отец', 'Мать', 'Сын', 'Дедушка']

    # список списков приблизительного роста членов семьи
    my_family_height = [
        ['Отец', 180],
        ['Мать', 165],
        ['Сын', 175],
        ['Сестра', 160],
    ]

    # Рост отца
    father_height = my_family_height[0][1]
    print(f'Рост отца - {father_height} см')

    # Общий рост семьи
    total_height = sum(person[1] for person in my_family_height)
    print(f'Общий рост моей семьи - {total_height} см')


if __name__ == '__main__':
    run()