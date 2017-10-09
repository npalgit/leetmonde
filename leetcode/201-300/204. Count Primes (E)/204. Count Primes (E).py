#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 204. Count Primes (E)
# Created by yangchao 18/04/2017


class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return 0
        primes = [2]
        for x in range(3, n):
            is_prime = True
            for y in primes:
                if y * y > x:
                    break
                if x % y == 0:
                    is_prime = False
                    break
            if is_prime:
                primes.append(x)
        return len(primes)

s = Solution()

print s.countPrimes(0), 0
print s.countPrimes(1), 0
print s.countPrimes(2), 0
print s.countPrimes(3), 1
print s.countPrimes(4), 2
print s.countPrimes(5), 2
print s.countPrimes(6), 3
print s.countPrimes(7), 3
print s.countPrimes(8), 4
print s.countPrimes(9), 4