#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 131. Palindrome Partitioning (M)
# Created by yangchao 20/04/2017


class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        print '--------'
        l = len(s)
        if l == 0:
            return []
