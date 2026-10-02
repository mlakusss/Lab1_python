#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Pytest-тесты для всех модулей-заданий лабораторной работы №1.

Каждый тест проверяет, что функция run() модуля выводит ожидаемые строки.
Импорт модулей с именами, начинающимися с цифр, выполняется через
importlib.import_module(), так как стандартный import невозможен.
"""

import importlib

import pytest


def _run(module_name):
    """Импортирует модуль по имени и вызывает его функцию run()."""
    module = importlib.import_module(module_name)
    importlib.reload(module)
    module.run()


# ---------------------------------------------------------------------------
# 00_distance
# ---------------------------------------------------------------------------
def test_distance(capsys):
    _run('00_distance')
    out = capsys.readouterr().out
    assert "'Moscow'" in out
    assert "'London'" in out
    assert "'Paris'" in out
    assert '145.6' in out
    assert '130.38' in out
    assert '42.43' in out


# ---------------------------------------------------------------------------
# 01_circle
# ---------------------------------------------------------------------------
def test_circle(capsys):
    _run('01_circle')
    out = capsys.readouterr().out
    lines = out.strip().splitlines()
    assert lines[0] == '5541.7693'
    assert lines[1] == 'True'
    assert lines[2] == 'False'


# ---------------------------------------------------------------------------
# 02_operations
# ---------------------------------------------------------------------------
def test_operations(capsys):
    _run('02_operations')
    out = capsys.readouterr().out
    lines = out.strip().splitlines()
    assert lines[0] == '9'
    assert lines[1] == '25'


# ---------------------------------------------------------------------------
# 03_favorite_movies
# ---------------------------------------------------------------------------
def test_favorite_movies(capsys):
    _run('03_favorite_movies')
    out = capsys.readouterr().out
    lines = out.strip().splitlines()
    assert lines == ['Терминатор', 'Назад в будущее', 'Пятый элемент', 'Чужие']


# ---------------------------------------------------------------------------
# 04_my_family
# ---------------------------------------------------------------------------
def test_my_family(capsys):
    _run('04_my_family')
    out = capsys.readouterr().out
    assert 'Рост отца - 180 см' in out
    assert 'Общий рост моей семьи - 680 см' in out


# ---------------------------------------------------------------------------
# 05_zoo
# ---------------------------------------------------------------------------
def test_zoo(capsys):
    _run('05_zoo')
    out = capsys.readouterr().out
    assert "['lion', 'bear', 'kangaroo', 'elephant', 'monkey']" in out
    assert "'lark'" in out
    assert '1 7' in out


# ---------------------------------------------------------------------------
# 06_songs_list
# ---------------------------------------------------------------------------
def test_songs_list(capsys):
    _run('06_songs_list')
    out = capsys.readouterr().out
    assert 'Три песни звучат 14.93 минут' in out
    assert 'А другие три песни звучат 13.49 минут' in out


# ---------------------------------------------------------------------------
# 07_secret
# ---------------------------------------------------------------------------
def test_secret(capsys):
    _run('07_secret')
    out = capsys.readouterr().out.strip()
    assert out == 'в бане веник дороже денег'


# ---------------------------------------------------------------------------
# 08_garden
# ---------------------------------------------------------------------------
def test_garden(capsys):
    _run('08_garden')
    out = capsys.readouterr().out
    assert 'Все виды цветов:' in out
    assert 'Растут и там, и там:' in out
    assert 'В саду, но не на лугу:' in out
    assert 'На лугу, но не в саду:' in out
    # конкретные элементы
    assert 'ромашка' in out
    assert 'клевер' in out
    assert 'гладиолус' in out


# ---------------------------------------------------------------------------
# 09_shopping
# ---------------------------------------------------------------------------
def test_shopping(capsys):
    _run('09_shopping')
    out = capsys.readouterr().out
    assert "'печенье'" in out
    assert "'пятерочка'" in out
    assert "'ашан'" in out
    # минимум у печенья — 9.99 (пятерочка)
    assert '9.99' in out


# ---------------------------------------------------------------------------
# 10_store
# ---------------------------------------------------------------------------
def test_store(capsys):
    _run('10_store')
    out = capsys.readouterr().out
    assert 'Лампа - 27 шт, стоимость 1134 руб' in out
    assert 'Стол - 54 шт, стоимость 27860 руб' in out
    assert 'Диван - 3 шт, стоимость 3550 руб' in out
    assert 'Стул - 105 шт, стоимость 10311 руб' in out