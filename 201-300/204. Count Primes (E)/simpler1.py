#!/usr/bin/env python
# -*- coding: utf-8 -*-

# simpler1
# Created by yangchao 18/04/2017


import time


class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return 0
        _set =[True for i in range(n)]
        x = 2
        ret = n - 2
        while x < n:
            if not _set[x]:
                x += 1
                continue
            if x * x >= n:
                break
            num = x + x
            while num < n:
                if _set[num]:
                    _set[num] = False
                    ret -= 1
                num += x
            x += 1

        return ret


s = Solution()

print s.countPrimes(5), 2
print s.countPrimes(6), 3
print s.countPrimes(7), 3
print s.countPrimes(8), 4
print s.countPrimes(9), 4
print s.countPrimes(10), 4
print s.countPrimes(100), 25
print s.countPrimes(1000), 168

print time.time()
print s.countPrimes(900000), 71274
print time.time()
print s.countPrimes(1500000), 114155
print time.time()

print s.countPrimes(0), 0
print s.countPrimes(1), 0
print s.countPrimes(2), 0
print s.countPrimes(3), 1
print s.countPrimes(4), 2