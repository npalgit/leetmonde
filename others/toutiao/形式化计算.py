#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 形式化计算
# Created by yangchao 18/04/2017


def read():
    input_str = raw_input()

    arr = input_str.split()
    return arr[0], arr[2], arr[1]


def operate(a, b, op):
    if op == '+':
        show(a, op, b, str(int(a) + int(b)))
    elif op == '-':
        show(a, op, b, str(int(a) - int(b)))
    elif op == '*':
        show(a, op, b, str(int(a) * int(b)))
    else:
        ai = int(a)
        bi = int(b)
        if ai/bi * bi == ai:
            show(a, op, b, str(ai / bi))
        else:
            ai += 0.0
            show(a, op, b, str(ai / bi))


def show(a, op, b, ret):
    letters = {
        '1': [
            '*',
            '*',
            '*',
            '*',
            '*',
        ],
        '2': [
            '***',
            '  *',
            '***',
            '*  ',
            '***',
        ],
        '3': [
            '***',
            '  *',
            '***',
            '  *',
            '***',
        ],
        '4': [
            '* *',
            '* *',
            '***',
            '  *',
            '  *',
        ],
        '5': [
            '***',
            '*  ',
            '***',
            '  *',
            '***',
        ],
        '6': [
            '***',
            '*  ',
            '***',
            '* *',
            '***',
        ],
        '7': [
            '***',
            '  *',
            '  *',
            '  *',
            '  *',
        ],
        '8': [
            '***',
            '* *',
            '***',
            '* *',
            '***',
        ],
        '9': [
            '***',
            '* *',
            '***',
            '* *',
            '***',
        ],
        '0': [
            '***',
            '* *',
            '* *',
            '* *',
            '***',
        ],
        '+': [
            '   ',
            ' * ',
            '***',
            ' * ',
            '   ',
        ],
        '-': [
            '   ',
            '   ',
            '***',
            '   ',
            '   ',
        ],
        '*': [
            '   ',
            '* *',
            ' * ',
            '* *',
            '   ',
        ],
        '/': [
            '   ',
            '  *',
            ' * ',
            '*  ',
            '   ',
        ],
        '=': [
            '    ',
            '****',
            '    ',
            '****',
            '    ',
        ],
        '.': [
            '  ',
            '  ',
            '  ',
            '**',
            '**',
        ]
    }
    for i in [0, 1, 2, 3, 4]:
        ret_str = []
        for s in a:
            ret_str.append(letters[s][i])
        # 操作符
        ret_str.append(letters[op][i])
        for s in b:
            ret_str.append(letters[s][i])
        # 等号
        ret_str.append(letters['='][i])
        for s in ret:
            ret_str.append(letters[s][i])
        print '  '.join(ret_str)

a, b, op = read()
operate(a, b, op)