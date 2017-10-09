#!/usr/bin/env python
# -*- coding: utf-8 -*-

# cathy
# Created by yangchao 18/04/2017


class Solution(object):
    def __init__(self):
        self.state_set = []
        self.n = 0

    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return 0
        self.state_set = [True for i in range(0, n)]
        self.n = n

        count = 0
        i = 2
        while i < n:
            if i * i > n:
                break
            if self.state_set[i]:
                self.eladuosai(i)
            i += 1
        self.state_set[2] = True
        for i in range(2, n):
            if self.state_set[i]:
                count += 1
        return count

    def eladuosai(self, num):
        i = num + num
        while i < self.n:
            self.state_set[i] = False
            i += num
        pass
test = Solution()
print test.countPrimes(1500000)

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