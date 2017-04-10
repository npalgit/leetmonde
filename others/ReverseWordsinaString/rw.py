#!/usr/bin/env python
# -*- coding: utf-8 -*-

# rw
# Created by yangchao 24/03/2017
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        a = s.split(' ')
        a.reverse()
        r = []
        for i in a:
            if i == '' or i == ' ':
                continue
            r.append(i)
        return ' '.join(r)

s = Solution()
print s.reverseWords("1   1")