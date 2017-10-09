#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 134. Gas Station (M)
# Created by yangchao 21/04/2017


class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        l = len(gas)
        start = 0
        while start < l:
            diff = 0
            current = start
            while diff >= 0:
                diff += gas[current] - cost[current]
                current = (current+1) % l
                if current == start:
                    if diff >= 0:
                        return start
                    else:
                        return -1
            if start < current:
                start = current
            else:
                return -1
        return -1




s = Solution()

print s.canCompleteCircuit([1, 3], [1, 2])
print s.canCompleteCircuit([2, 6], [3, 2])
print s.canCompleteCircuit([5], [4])
print s.canCompleteCircuit([1], [4])
print s.canCompleteCircuit([1, 3, 2, 3], [5, 1, 2, 1])
print s.canCompleteCircuit([1, 3, 3, 2, 1, 3, 4], [5, 1, 1, 1, 5, 1, 1])
print s.canCompleteCircuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2])
print s.canCompleteCircuit([6, 0, 1,3,2], [4,5,2,5,5])
