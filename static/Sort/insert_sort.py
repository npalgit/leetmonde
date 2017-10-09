#!/usr/bin/env python
# -*- coding: utf-8 -*-

# insert_sort
# Created by yangchao 2017/10/9


def insert_sort(_list):
    l = len(_list)
    if l < 2:
        return _list
    ret = [_list[0]]
    for i in range(1, l):
        x = _list[i]

        flag = False
        for j in range(len(ret)):
            if x < ret[j]:
                ret.insert(j, x)
                flag = True
                break

        if not flag:
            ret.append(x)
    return ret


if __name__ == '__main__':

    a = [[9, 2, 3, 4, 5, 7],
         [8, 3, 4, 1, 3, 0, 9, 3, 2],
         [9, 8, 7, 6, 5, 4, 3, 2, 1],
         [9],
         []]
    for x in a:
        print x
        print insert_sort(x)
        print '========'
