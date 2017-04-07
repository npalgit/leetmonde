#!/usr/bin/env python
# -*- coding: utf-8 -*-

# lis
# Created by yangchao 07/04/2017
import copy
class Solution(object):
    def lis(self, nums):
        # n^3
        print self.n3(nums)
        return self.n2(nums)

    def n3(self, nums):

        l = len(nums)
        if l < 1:
            return 0
        last = set()
        temp = set()
        max = 1
        for i, val in enumerate(nums):
            last.add(i)
            step = 1
            while last:
                temp.clear()
                for a in last:
                    for j in range(a+1, l):
                        if nums[j] > nums[a]:
                            temp.add(j)
                if temp:
                    step += 1
                    if step > max:
                        max = step
                    last = copy.deepcopy(temp)
                else:
                    break
        return max

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


s = Solution()
print s.lis([0])   # 1
print s.lis(range(2))
print s.lis([1, 1, 0, 3, 2, 3, 4, 5, 4, 7, 6, 4])   # 1

print s.lis([])   # 0
print s.lis([0, 1])   # 2
print s.lis([2, 1])   # 1