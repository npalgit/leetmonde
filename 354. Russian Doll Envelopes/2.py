#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 354. Russian Doll Envelopes
# Created by yangchao 07/04/2017


import time
class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        def compare(a, b):
            return 1 if a[0] > b[0] or (a[0] == b[0] and a[1] < b[1]) else -1

        l = len(envelopes)
        if l < 1:
            return 0
        envelopes.sort(cmp=compare)

        arr = []
        for item in envelopes:
            arr.append(item[1])
        return self.n2(arr)

    def n2(self, nums):

        def lmip(envs, tails, k):
            b, e = 0, len(tails) - 1
            while b <= e:
                m = (b + e) >> 1
                if envs[tails[m]] >= k:
                    e = m - 1
                else:
                    b = m + 1
            return b

        tails = []
        for i, env in enumerate(nums):
            idx = lmip(nums, tails, env)
            if idx >= len(tails):
                tails.append(i)
            else:
                tails[idx] = i
        return len(tails)




s = Solution()
print s.maxEnvelopes([])  # 0
print s.maxEnvelopes([[2, 3]])  # 1
print s.maxEnvelopes([[5, 4], [6, 7], [6, 4], [2, 3]])  # 3
print s.maxEnvelopes([[1, 1000], [0, 0], [1, 1], [2, 3]])  # 3
print s.maxEnvelopes(
    [[5, 4], [6, 7], [6, 4], [6, 6], [5, 5], [4, 4], [3, 3], [2, 3], [2, 2], [1, 1], [1, 0], [0, 1]])  # 6

print s.maxEnvelopes([[5, 4], [6, 7], [6, 4], [2, 3]])  # 3



from bigger import a
print time.time()
print s.maxEnvelopes(a)
print time.time()
