#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def run():
    goods = {
        'Лампа': '12345',
        'Стол': '23456',
        'Диван': '34567',
        'Стул': '45678',
    }

    store = {
        '12345': [{'quantity': 27, 'price': 42}],
        '23456': [
            {'quantity': 22, 'price': 510},
            {'quantity': 32, 'price': 520},
        ],
        '34567': [
            {'quantity': 2, 'price': 1200},
            {'quantity': 1, 'price': 1150},
        ],
        '45678': [
            {'quantity': 50, 'price': 100},
            {'quantity': 12, 'price': 95},
            {'quantity': 43, 'price': 97},
        ],
    }

    for name, code in goods.items():
        batches = store[code]
        total_quantity = sum(b['quantity'] for b in batches)
        total_cost = sum(b['quantity'] * b['price'] for b in batches)
        print(f'{name} - {total_quantity} шт, стоимость {total_cost} руб')


if __name__ == '__main__':
    run()