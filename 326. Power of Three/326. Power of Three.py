#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 326. Power of Three
# Created by yangchao 25/03/2017
class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n in [1, 3, 9, 27, 81, 243, 729, 2187, 6561, 19683, 59049, 177147, 531441, 1594323, 4782969, 14348907, 43046721, 129140163, 387420489, 1162261467, 3486784401]

    def support(self):
        x = []
        a = 3
        for i in range(0, 20):
            x.append(a)
            a *= 3
        print(x)


s = Solution()
# s.support()
print(s.isPowerOfThree(27)) # true
print(s.isPowerOfThree(28)) # False

print(s.deleteDuplicates([]))