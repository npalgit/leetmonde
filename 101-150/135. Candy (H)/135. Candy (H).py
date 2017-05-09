#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 135. Candy (H)
# Created by yangchao 09/05/2017


class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        length = len(ratings)
        if length == 0:
            return 0
        l0 = [1]
        l1 = [1]
        for i in range(1, length):
            if ratings[i] > ratings[i-1]:
                l0.append(l0[i-1]+1)
            else:
                l0.append(1)

        for i in range(length-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                l1.append(l1[length-i-2]+1)
            else:
                l1.append(1)
        ret = 0
        for i in range(length):
            ret += max(l0[i], l1[length-i-1])
        return ret

s = Solution()
print s.candy([2, 3, 2]), 4
print s.candy([1, 2, 1, 3, 1, 4, 1, 5]), 12
print s.candy([]), 0
print s.candy([1]), 1
print s.candy([1, 2]), 3