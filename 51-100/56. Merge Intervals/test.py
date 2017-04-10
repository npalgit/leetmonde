#!/usr/bin/env python
# -*- coding: utf-8 -*-

# test
# Created by yangchao 08/04/2017


a = [3, 4, 1, 2]
import copy
b = copy.deepcopy(a)
c = copy.deepcopy(a)

a.sort()
print a

def cm(a, b):
    if a > b:
        return 1
    return -1
b.sort(cm)
print b

def cm(b, a):
    if a > b:
        return 1
    return -1
c.sort(cm)
print c


