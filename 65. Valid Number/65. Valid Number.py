#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 65. Valid Number
# Created by yangchao 29/03/2017
import re
class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.strip()
        if len(s) == 0:
            return False
        reg = r'^(-|\+)?([0-9]*\.?[0-9]+|[0-9]+\.?)(e(-|\+)?[0-9]+)?$'
        r = re.match(reg, s)
        return r is not None

s = Solution()
print s.isNumber(' ')
print s.isNumber('e')
print s.isNumber('1 1')
print s.isNumber('1e')
print s.isNumber('e1')
print s.isNumber('.')
print s.isNumber('3.')
print s.isNumber('3.e10')
print s.isNumber('.3e-10')
print s.isNumber('+.3e-10')
print s.isNumber('+.3')