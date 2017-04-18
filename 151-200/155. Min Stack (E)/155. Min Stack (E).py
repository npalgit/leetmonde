#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 155. Min Stack (E)
# Created by yangchao 17/04/2017

import heapq


class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.container = []
        self.min = None
        self.length = 0

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.length += 1
        if self.min is None or x < self.min:
            self.min = x
        self.container.append(x)

    def pop(self):
        """
        :rtype: void
        """
        if self.length < 1:
            return None
        self.length -= 1
        x = self.container.pop()
        if self.length == 0:
            self.min = None
        elif x == self.min:
            _min = self.container[0]
            for t in self.container:
                if _min > t:
                    _min = t
            self.min = _min
        return None

    def top(self):
        """
        :rtype: int
        """
        return self.container[self.length-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.min

from test import t1, run

run(MinStack, t1)