#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 115. Distinct Subsequences (H)
# Created by yangchao 16/04/2017


class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        m = len(s)
        if m == 0:
            return 0
        n = len(t)
        if n == 0:
            return 1
        mapping = [[0 for col in range(m+1)] for row in range(n+1)]
        for col in range(m + 1):
            mapping[0][col] = 1

        for row in range(1, n+1):
            t_char = t[row-1]
            for col in range(row, m+1):
                s_char = s[col-1]
                mapping[row][col] = mapping[row][col-1]
                if t_char == s_char:
                    mapping[row][col] = mapping[row-1][col-1] + mapping[row][col-1]
        return mapping[n][m]

s = Solution()

print s.numDistinct('abcde', 'ace'), 1
print s.numDistinct('rabbbit', 'rabbbit'), 1
print s.numDistinct('rabbbit', 'rabbit'), 3
print s.numDistinct('rabbbit', 'rabit'), 3