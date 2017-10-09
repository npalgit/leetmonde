#!/usr/bin/env python
# -*- coding: utf-8 -*-

# quick_sort
# Created by yangchao 2017/10/9


def process(_list, start, end):
    if start > end:
        return
    temp = _list[start]
    i = start
    j = end

    while i < j:
        if _list[j] >= temp:
            j -= 1
            continue
        if _list[i] <= temp:
            i += 1
            continue
        _list[i], _list[j] = _list[j], _list[i]
        j -= 1
    if _list[i] < temp:
        _list[start], _list[i] = _list[i], _list[start]

    process(_list, start, i - 1)
    process(_list, i + 1, end)
    return _list


def quick_sort(_list):
    l = len(_list)
    if l < 2:
        return _list
    return process(_list, 0, l-1)


if __name__ == '__main__':
    a = [9, 2, 3, 4, 5, 7]
    b = [8, 3, 4, 1, 3, 0, 9, 3, 2]
    c = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    d = [9]
    e = []
    print quick_sort(c)
    print quick_sort(b)
    print quick_sort(a)
    print quick_sort(d)
    print quick_sort(e)
