#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 形式化计算
# Created by yangchao 18/04/2017


def read():
    input_str = raw_input()

    arr = input_str.split()
    str_nums = [arr[0]]
    nums = [int(arr[0])]
    op = []
    i = 1
    l = len(arr)
    while i < l:
        op.append(arr[i])
        i += 1
        str_nums.append(arr[i])
        nums.append(int(arr[i]))
        i += 1
    return nums, op, str_nums


def operate(nums, ops):
    _stack = []
    l = len(nums)
    l1 = len(ops)
    i = 0
    j = 0

    a = nums[i]
    while i < l - 1 and j < l1:
        op = ops[j]
        if op == '-' or op == '+':
            _stack.append((a, op))
            i += 1
            a = nums[i]

            j += 1
            continue
        elif op == '*':
            i += 1
            b = nums[i]
            a = a * b

            j += 1
            continue
        else:
            i += 1
            b = nums[i] + 0.0
            a /= b

            j += 1
            continue
    while _stack:
        b = _stack.pop()
        if b[1] == '-':
            a = b[0] - a
        elif b[1] == '+':
            a += b[0]
    inta = int(a)
    if a == inta:
        return str(inta)
    return str(a)


def show(_str_nums, _ops, _ret):
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
        l = len(_str_nums)

        for j in range(l-1):
            for s in _str_nums[j]:
                ret_str.append(letters[s][i])
            ret_str.append(letters[_ops[j]][i])
        for s in _str_nums[l-1]:
            ret_str.append(letters[s][i])
        ret_str.append(letters['='][i])
        for s in _ret:
            ret_str.append(letters[s][i])

        print '  '.join(ret_str)

nums, ops, str_nums = read()
ret = operate(nums, ops)
show(str_nums, ops, ret)