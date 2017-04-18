#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ttest
# 单次加法比乘法快
# Created by yangchao 18/04/2017

import time


def test(num, base=5):
    ret = 1
    ret1 = 0
    print time.time()
    for i in range(num):
        ret = i * base
        ret = i * base
    print time.time(), ret
    for i in range(num):
        ret1 += base
        ret1 += base
    print time.time(), ret1

test(5000000)