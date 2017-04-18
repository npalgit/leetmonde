#!/usr/bin/env python
# -*- coding: utf-8 -*-

# test
# Created by yangchao 18/04/2017


t1 = [["MinStack", "push", "push", "push", "getMin", "pop", "top", "getMin"],
      [[], [-2], [0], [-3], [], [], [], []]]


def run(MinStack, test):
    s = MinStack()
    operations = test[0][1:]
    params = test[1][1:]
    for i, x in enumerate(operations):
        if x == 'push':
            print s.push(params[i][0]), x
        elif x == 'getMin':
            print s.getMin(), x
        elif x == 'pop':
            print s.pop(), x
        elif x == 'top':
            print s.top(), x
