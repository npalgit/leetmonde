#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 72. Edit Distance
# Created by yangchao 01/04/2017


class Solution(object):

    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        l1 = len(word1)
        l2 = len(word2)
        if l1 == 0:
            return l2
        if l2 == 0:
            return l1
        l1 += 1
        l2 += 1
        mat = [[j for j in range(l2)] for i in range(l1)]
        for i in range(l1):
            mat[i][0] = i

        for i in range(1, l1):
            i_ = i - 1
            letter1 = word1[i_]
            for j in range(1, l2):
                j_ = j - 1
                letter2 = word2[j_]
                if letter1 != letter2:
                    steps = mat[i_][j_] + 1
                else:
                    steps = mat[i_][j_]
                if steps > mat[i][j_] + 1:
                    steps = mat[i][j_] + 1
                if steps > mat[i_][j] + 1:
                    steps = mat[i_][j] + 1
                mat[i][j] = steps
        return mat[l1-1][l2-1]


s = Solution()
print s.minDistance('cnblogs', 'belong') # 5
print s.minDistance('', '') # 0
print s.minDistance('大众高尔夫 2016款 1.4TSI 自动豪华型', '大众高尔夫 2016款 230TSI 自动豪华型') # 0