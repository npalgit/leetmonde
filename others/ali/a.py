#!/usr/bin/env python
# -*- coding: utf-8 -*-

# a
# Created by yangchao 2017/8/25
import math
# y = 2a * a + a
# y = 2a * a - a
"""
1   2   3   4   5   6   7   8   9   10  11 ...  51  52  53  54  55  56  57  58  ... 92  93  94  95  96  97  98  99  100
1   1   2   1   2   3   1   2   3   4   1  ...  6   7   8   9   1   0   1   2   ... 8   9   1   0   1   1   1   2   1

"""


def _pro(y):
    if y < 1 or y is None or not isinstance(y, int):
        return None
    delta = math.sqrt(0.25 + 2*y) / 2
    bottom = int(2 * (-0.25 + delta))
    r = bottom*(bottom+1)/2

    if r == y:
        c = bottom
    else:
        c = y - r

    if y - r - c == 0:
        round_num = bottom + 1
    else:
        round_num = bottom
    return c, round_num


def process(y):
    # c 是真实值, round_num 是轮次
    c, round_num = _pro(y)
    _y = y
    _rich = 0
    for x in range(10, round_num+1):
        for z in range(10, x+1):
            if x == round_num and z > c:
                break
            true_pos = calc(z, x)
            l = len(str(z)) - 1
            if _y > true_pos + l:
                _y -= l
            elif _y > true_pos:
                _rich = _y - true_pos
                _y -= l
                break
            elif _y <= true_pos:
                break
    return str(_pro(_y)[0])[_rich]


def calc(index, round_num):
    return round_num*(round_num-1)/2 + index

for _ in range(1, 100):
    print _, process(_)


