#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 任务执行策略
# Created by yangchao 18/04/2017


def read():
    input_str = raw_input()
    arr = input_str.split()
    n = int(arr[0])
    k = int(arr[1])

    mes = []
    for i in range(n):
        input_str = raw_input()
        arr = input_str.split()
        _arr = []
        for j, x in enumerate(arr):
            _arr.append([i, j, int(x)])

        def cmp(a, b):
            return -1 if a[2]>b[2] else 1
        _arr.sort(cmp)
        mes.append(_arr)
    return n, k, mes


def solution(n, k, mes):

    if k == 0:
        return 0
    if n * n /2 == k:
        ret = 0
        for line in mes:
            for x in line:
                ret += x[2]
        return ret

def process()




n, k, mes = read()
print solution(n, k, mes)
