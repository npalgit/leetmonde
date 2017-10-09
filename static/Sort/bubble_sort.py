#!/usr/bin/env python
# -*- coding: utf-8 -*-

# blob_sort
# Created by yangchao 2017/10/9


def bubble_sort(_list):
    l = len(_list)
    if l < 2:
        return _list

    for i in range(l - 1):
        flag = False
        for j in range(l - 1):
            if _list[j] > _list[j + 1]:
                _list[j], _list[j + 1] = _list[j + 1], _list[j]
                flag = True
        if not flag:
            return _list
    return _list


if __name__ == '__main__':
    a = [[9, 2, 3, 4, 5, 7],
         [8, 3, 4, 1, 3, 0, 9, 3, 2],
         [9, 8, 7, 6, 5, 4, 3, 2, 1],
         [9],
         []]
    for x in a:
        print x
        print bubble_sort(x)
        print '========'
