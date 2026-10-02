#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def run():
    my_favorite_movies = 'Терминатор, Пятый элемент, Аватар, Чужие, Назад в будущее'

    print(my_favorite_movies[:10])        # Терминатор
    print(my_favorite_movies[42:])        # Назад в будущее
    print(my_favorite_movies[12:25])      # Пятый элемент
    print(my_favorite_movies[35:40])      # Чужие


if __name__ == '__main__':
    run()