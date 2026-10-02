#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def run():
    garden = ('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза', )
    meadow = ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка', )

    garden_set = set(garden)
    meadow_set = set(meadow)

    print('Все виды цветов:', garden_set | meadow_set)
    print('Растут и там, и там:', garden_set & meadow_set)
    print('В саду, но не на лугу:', garden_set - meadow_set)
    print('На лугу, но не в саду:', meadow_set - garden_set)


if __name__ == '__main__':
    run()