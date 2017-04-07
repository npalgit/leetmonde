#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 22. Generate Parentheses
# Created by yangchao 28/03/2017
import copy
class Solution(object):
    def __init__(self):
        self.result = []

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.process(0, n, [])
        return self.result

    def process(self, count, n, arr):
        if count < 0 or count > n:
            return

        if len(arr) == 2*n:
            if count == 0:
                self.result.append(''.join(arr))
            return
        arr1 = copy.deepcopy(arr)
        arr1.append('(')
        self.process(count+1, n, arr1)

        arr2 = copy.deepcopy(arr)
        arr2.append(')')
        self.process(count-1, n, arr2)

s = Solution()
print(s.generateParenthesis(3))
### [ "((()))", "(()())", "(())()", "()(())", "()()()" ]
