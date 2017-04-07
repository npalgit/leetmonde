#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 354. Russian Doll Envelopes
# Created by yangchao 07/04/2017


class Solution(object):
    def __init__(self):
        self.max_degree = {}
        self.mapping0 = {}
        self.max = 1

    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        l = len(envelopes)
        if l < 1:
            return 0
        self.max_degree = {}
        self.mapping0 = {}
        self.max = 1

        for item in envelopes:
            key = (item[0], item[1])
            self.mapping0[key] = set()
            self.max_degree[key] = 0

        for i, item in enumerate(envelopes):
            key = (item[0], item[1])
            for j in range(i + 1, l):
                envelope = envelopes[j]
                new_key = (envelope[0], envelope[1])
                if item[0] < envelope[0] and item[1] < envelope[1]:
                    self.mapping0[new_key].add(key)
                if item[0] > envelope[0] and item[1] > envelope[1]:
                    self.mapping0[key].add(new_key)
        self.findMax()

        return self.max

    def findMax(self):
        for i in self.max_degree:
            item = self.max_degree[i]
            if item:
                continue
            self._process(i)

    def _process(self, node):
        if self.max_degree[node]:
            return
        children = self.mapping0[node]
        if len(children) == 0:
            self.max_degree[node] = 1
            return
        max_degree = 0
        for key in children:
            if self.max_degree[key] == 0:
                self._process(key)
            if max_degree < self.max_degree[key]:
                max_degree = self.max_degree[key]
        self.max_degree[node] = 1 + max_degree
        if self.max_degree[node] > self.max:
            self.max = self.max_degree[node]


s = Solution()

from bigger import a
import time

print len(a)
print time.time()
print s.maxEnvelopes(a)
print time.time()

exit()
print s.maxEnvelopes([])  # 0
print s.maxEnvelopes([[2, 3]])  # 1
print s.maxEnvelopes([[5, 4], [6, 7], [6, 4], [2, 3]])  # 3
print s.maxEnvelopes([[1, 1000], [0, 0], [1, 1], [2, 3]])  # 3
print s.maxEnvelopes(
    [[5, 4], [6, 7], [6, 4], [6, 6], [5, 5], [4, 4], [3, 3], [2, 3], [2, 2], [1, 1], [1, 0], [0, 1]])  # 6
