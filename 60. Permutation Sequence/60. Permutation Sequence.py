#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 60. Permutation Sequence
# Created by yangchao 09/04/2017


class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        if n < 1:
            return ''
        if n == 1:
            return '1'

        steps = []
        last = 1
        for i in range(1, n):
            last *= i
            steps.append(last)

        ret = []
        nums = range(n+1)
        k -= 1
        while steps:
            weight = steps.pop()
            index = k/weight + 1
            ret.append(nums[index])

            temp = nums.pop()
            if len(nums) > index:
                nums[index] = temp
            nums.sort()
            k %= weight
        ret.append(nums[1])
        return ''.join([str(x) for x in ret])






s = Solution()

print s.getPermutation(1, 1)    # 1
print s.getPermutation(2, 2)    # 21
print s.getPermutation(3, 2)    # 132
print s.getPermutation(4, 2)    # 1243
print s.getPermutation(4, 7)    # 2134
