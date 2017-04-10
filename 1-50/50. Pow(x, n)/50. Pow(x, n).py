#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 50. Pow(x, n)
# Created by yangchao 08/04/2017


class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if x == 0:
            return 0
        if n == 0:
            return 1
        if n == 1:
            return x

        nag = False
        if n < 0:
            n = 0 - n
            nag = True

        _n = n / 2
        _ret = self.myPow(x, _n)
        ret = _ret * _ret
        if n % 2 == 1:
            ret *= x

        if nag:
            return 1 / ret
        return ret
