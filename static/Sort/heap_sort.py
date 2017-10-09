#!/usr/bin/env python
# -*- coding: utf-8 -*-

# heap_sort
# Created by yangchao 2017/10/9


def heap_adjust(_list, k, n):
    temp = _list[k]

    while 2 * k + 1 < n:
        j = 2 * k + 1
        if j + 1 < n and _list[j] < _list[j + 1]:  # 选出左右孩子节点中更大的那个
            j += 1
        if temp >= _list[j]:
            break

        _list[k] = _list[j]
        k = j
    _list[k] = temp


def heap_sort(_list):
    n = len(_list)
    if n < 2:
        return _list

    for i in range(n / 2, -1, -1):
        heap_adjust(_list, i, n)

    while n > 0:
        _list[0], _list[n-1] = _list[n-1], _list[0]
        n -= 1
        heap_adjust(_list, 0, n)
    return _list

if __name__ == '__main__':

    a = [[9, 2, 3, 4, 5, 7],
         [8, 3, 4, 1, 3, 0, 9, 3, 2],
         [9, 8, 7, 6, 5, 4, 3, 2, 1],
         [9],
         []]
    for x in a:
        print x
        print heap_sort(x)
        print '========'
