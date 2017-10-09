#!/usr/bin/env python
# -*- coding: utf-8 -*-

# find_kth_number
# Created by yangchao 2017/10/9

from quick_sort import quick_sort


def process(_list, start, end):
    if start > end:
        return _list, start

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
    if temp > _list[i]:
        _list[start], _list[i] = _list[i], _list[start]
    return _list, i


def find_kth_number(_list, k):
    l = len(_list)
    if l < 1 or k > l:
        return None
    index = l - k

    start = 0
    end = l - 1
    new_list, new_index = process(_list, start, end)
    while index != new_index:
        if new_index > index:
            end = new_index - 1
        else:
            start = new_index + 1

        new_list, new_index = process(new_list, start, end)
    return new_list[new_index]


if __name__ == '__main__':
    a = [[9, 2, 3, 4, 5, 7],
         [8, 3, 4, 1, 3, 0, 9, 3, 2],
         [9, 8, 7, 6, 5, 4, 3, 2, 1],
         [9],
         []]
    for x in a:
        print x
        print quick_sort(x)
        ret = []
        ret1 = []
        length = len(x)
        for _i in range(length):
            ret.append(find_kth_number(x, _i+1))
            ret1.append(find_kth_number(x, length-_i))
        print ret
        print ret1
        print '============'
