#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 10. Regular Expression Matching
# Created by yangchao 06/04/2017
import re
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        matches = re.findall('^'+p+'$', s)
        if len(matches) > 0:
            return True
        return False