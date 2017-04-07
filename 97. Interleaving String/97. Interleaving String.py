#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 97. Interleaving String
# Created by yangchao 31/03/2017
class Solution(object):
    def __init__(self):
        self.s1 = ''
        self.s2 = ''
        self.s3 = ''
        self.result = False
        self.count = 0

    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        l1 = len(s1)
        l2 = len(s2)
        l3 = len(s3)
        if l3 != l1+l2:
            return False
        self.result = False
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3
        self.process(l1-1, l2-1, l3-1)
        return self.result

    def process(self, l1, l2, l3):
        self.count += 1
        if self.result:
            return True
        if l3 == -1:
            if l1 == -1 and l2 == -1:
                self.result = True
                return True
            self.result = False
            return False
        letter = self.s3[l3]
        if l1 > -1:
            letter1 = self.s1[l1]
            if letter == letter1:
                self.process(l1 - 1, l2, l3 - 1)
        if l2 > -1:
            letter2 = self.s2[l2]
            if letter == letter2:
                self.process(l1, l2 - 1, l3 - 1)
        if l1 < 0 and l2 < 0:
            self.result = False
            return False

s = Solution()
print s.isInterleave("aabcc", "dbbca", "aadbbcbcac") # True
print s.isInterleave("aabcc", "dbbca", "aadbbbaccc") # False
print s.isInterleave("", "", "") # False
print s.isInterleave("", "1", "") # False
print s.isInterleave("", "1", "1") # True
import time
print time.time()
print s.isInterleave("baababbabbababbaaababbbbbbbbbbbaabaabaaaabaaabbaaabaaaababaabaaabaabbbbaabbaabaabbbbabbbababbaaaabab",
"aababaaabbbababababaabbbababaababbababbbbabbbbbababbbabaaaaabaaabbabbaaabbababbaaaababaababbbbabbbbb",
"babbabbabbababbaaababbbbaababbaabbbbabbbbbaaabbabaababaabaaabaabbbaaaabbabbaaaaabbabbaabaaaabbbbababbbababbabaabababbababaaaaaabbababaaabbaabbbbaaaaabbbaaabbbabbbbaaabaababbaabababbbbababbaaabbbabbbab") # True
print time.time()
print s.count