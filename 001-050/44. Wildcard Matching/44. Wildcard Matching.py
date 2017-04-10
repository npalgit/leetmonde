#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 44. Wildcard Matching
# Created by yangchao 03/04/2017
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        length_string = len(s)
        length_pattern = len(p)

        string_begin = 0
        string_end = length_string - 1

        pattern = []
        max_val = []
        pattern[0] = []
        pattern[1] = []
        max_val[0] = 0
        max_val[1] = 0