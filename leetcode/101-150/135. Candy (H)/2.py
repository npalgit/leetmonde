#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 2
# Created by yangchao 04/08/2017


class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        l = len(ratings)
        if l < 1:
            return 0
        ret = [1 for i in range(l)]
        for i in range(1, l):
            if ratings[i] > ratings[i-1]:
                ret[i] = ret[i-1] + 1
        for i in range(l-2, -1, -1):
            if ratings[i] > ratings[i+1] and ret[i] <= ret[i+1]:
                ret[i] = ret[i+1]+1
        return sum(ret)


if __name__ == '__main__':
    s = Solution()

    print s.candy([]), 0
    print s.candy([1]), 1
    print s.candy([2, 1, 1]), 4
    print s.candy([4, 3, 4]), 5
    print s.candy([3, 2, 1, 2, 4, 3, 2, 1]), 18
    print s.candy([1, 2, 3, 4, 5, 2, 1]), 18
