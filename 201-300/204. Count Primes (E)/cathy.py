#!/usr/bin/env python
# -*- coding: utf-8 -*-

# cathy
# Created by yangchao 18/04/2017


class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return 0
        state_set = [True for i in range(0, n)]

        count = 0
        i = 2
        while i < n:
            if i * i > n:
                break
            if state_set[i]:
                num = i + i
                while num < n:
                    state_set[num] = False
                    num += i
            i += 1
        state_set[2] = True
        for i in range(2, n):
            if state_set[i]:
                count += 1
        return count

s = Solution()
import time
print time.time()
print s.countPrimes(900000), 71274
print s.countPrimes(100), 25
print s.countPrimes(1000), 168
print time.time()
print s.countPrimes(900000), 71274
print time.time()
print s.countPrimes(1500000), 114155
print time.time()