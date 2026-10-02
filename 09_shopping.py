#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def run():
    shops = {
        'ашан': [
            {'name': 'печенье', 'price': 10.99},
            {'name': 'конфеты', 'price': 34.99},
            {'name': 'карамель', 'price': 45.99},
            {'name': 'пирожное', 'price': 67.99}
        ],
        'пятерочка': [
            {'name': 'печенье', 'price': 9.99},
            {'name': 'конфеты', 'price': 32.99},
            {'name': 'карамель', 'price': 46.99},
            {'name': 'пирожное', 'price': 59.99}
        ],
        'магнит': [
            {'name': 'печенье', 'price': 11.99},
            {'name': 'конфеты', 'price': 30.99},
            {'name': 'карамель', 'price': 41.99},
            {'name': 'пирожное', 'price': 62.99}
        ],
    }

    sweets = {}
    for shop_name, products in shops.items():
        for product in products:
            name = product['name']
            price = product['price']
            sweets.setdefault(name, []).append(
                {'shop': shop_name, 'price': price}
            )

    # оставляем по 2 магазина с минимальными ценами
    for name in sweets:
        sweets[name] = sorted(sweets[name], key=lambda x: x['price'])[:2]

    print(sweets)


if __name__ == '__main__':
    run()