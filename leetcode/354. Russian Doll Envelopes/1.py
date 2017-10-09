#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 354. Russian Doll Envelopes
# Created by yangchao 07/04/2017


import time
class Solution(object):
    def __init__(self):
        self.envelopes = []

    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        l = len(envelopes)
        if l < 1:
            return 0
        self.envelopes = envelopes
        self.quickSort(0, l-1)
        arr = []
        for item in self.envelopes:
            arr.append(item[1])
        return self.n2(arr)

    def n2(self, nums):
        l = len(nums)
        if l < 1:
            return 0
        max_len = 1
        seq_len = [1 for i in range(l)]
        for i in range(1, l):
            temp_max = 0
            for j in range(i):
                if nums[j] < nums[i] and seq_len[j] > temp_max:
                    temp_max = seq_len[j]
            seq_len[i] = temp_max + 1
            if seq_len[i] > max_len:
                max_len = seq_len[i]
        return max_len

    def quickSort(self, b, e):
        begin = b
        end = e
        key = self.envelopes[b]
        b += 1
        while b <= e:
            if self.compare(self.envelopes[e], key):
                e -= 1
                continue
            if self.compare(key, self.envelopes[b]):
                b += 1
                continue
            self.envelopes[b], self.envelopes[e] = self.envelopes[e], self.envelopes[b]
        self.envelopes[e], self.envelopes[begin] = key, self.envelopes[e]

        if e > 1:
            self.quickSort(0, e)
        if b < end - 1:
            self.quickSort(b, end)

    def compare(self, a, b):
        return a[0] > b[0] or (a[0] == b[0] and a[1] < b[1])


s = Solution()
print s.maxEnvelopes([])  # 0
print s.maxEnvelopes([[2, 3]])  # 1
print s.maxEnvelopes([[5, 4], [6, 7], [6, 4], [2, 3]])  # 3
print s.maxEnvelopes([[1, 1000], [0, 0], [1, 1], [2, 3]])  # 3
print s.maxEnvelopes(
    [[5, 4], [6, 7], [6, 4], [6, 6], [5, 5], [4, 4], [3, 3], [2, 3], [2, 2], [1, 1], [1, 0], [0, 1]])  # 6

print s.maxEnvelopes([[5, 4], [6, 7], [6, 4], [2, 3]])  # 3


exit()
from bigger import a
print time.time()
print s.maxEnvelopes(a[1:30])
print time.time()
