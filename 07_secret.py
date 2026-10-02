#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def run():
    secret_message = [
        'квевтфпп6щ3стмзалтнмаршгб5длгуча',
        'дьсеы6лц2бане4т64ь4б3ущея6втщл6б',
        'т3пплвце1н3и2кд4лы12чф1ап3бкычаь',
        'ьд5фму3ежородт9г686буиимыкучшсал',
        'бсц59мегщ2лятьаьгенедыв9фк9ехб1а',
    ]

    word_1 = secret_message[0][3]
    word_2 = secret_message[1][9:13]
    word_3 = secret_message[2][5:15:2]
    word_4 = secret_message[3][12:6:-1]
    word_5 = secret_message[4][20:15:-1]

    result = f'{word_1} {word_2} {word_3} {word_4} {word_5}'
    print(result)


if __name__ == '__main__':
    run()