#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 20. Valid Parentheses
# Created by yangchao 28/03/2017
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        arr = []
        for i in s:
            if i == '(':
                arr.append(')')
            elif i == '{':
                arr.append('}')
            elif i == '[':
                arr.append(']')
            elif len(arr) == 0 or arr.pop() != i:
                return False
        if len(arr) != 0:
            return False
        return True