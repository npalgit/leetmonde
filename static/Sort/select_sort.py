#!/usr/bin/env python
# -*- coding: utf-8 -*-

# select_sort
# Created by yangchao 2017/10/9


def select_sort(_list):
    """
    :param _list: list
    :return:
    """
    l = len(_list)
    if l < 2:
        return _list

    ret = []

    for i in range(l):
        min_index = 0
        for j in range(len(_list)):
            if _list[min_index] > _list[j]:
                min_index = j
        ret.append(_list[min_index])
        del _list[min_index]
    return ret


if __name__ == '__main__':

    a = [[9, 2, 3, 4, 5, 7],
         [8, 3, 4, 1, 3, 0, 9, 3, 2],
         [9, 8, 7, 6, 5, 4, 3, 2, 1],
         [9],
         []]
    for x in a:
        print x
        print select_sort(x)
        print '========'



