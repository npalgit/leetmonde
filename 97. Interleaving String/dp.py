#!/usr/bin/env python
# -*- coding: utf-8 -*-

# dp
# Created by yangchao 31/03/2017
class Solution(object):
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
        print l1, l2, l3
        if l3 == 0:
            if l1 == 0 and l2 == 0:
                return True
            return False
        last = {(-1, -1):0}
        for i in range(0, l3):
            letter = s3[i]
            temp = {}
            for item in last:
                row = item[0]
                row1 = row + 1
                col = item[1]
                col1 = col + 1
                if row1 < l1 and s1[row1] == letter:
                    temp[(row1, col)] = 0
                if col1 < l2 and s2[col1] == letter:
                    temp[(row, col1)] = 0
            if len(temp) == 0:
                return False
            last = temp
        return True

import time
s = Solution()
print time.time()
print s.isInterleave("abbbbbbcabbacaacccababaabcccabcacbcaabbbacccaaaaaababbbacbb",
"ccaacabbacaccacababbbbabbcacccacccccaabaababacbbacabbbbabc",
"cacbabbacbbbabcbaacbbaccacaacaacccabababbbababcccbabcabbaccabcccacccaabbcbcaccccaaaaabaaaaababbbbacbbabacbbacabbbbabc") # True
print time.time()
print s.isInterleave("a", "", "c") # False
print s.isInterleave("aabcc", "dbbca", "aadbbcbcac") # True
print s.isInterleave("aabcc", "dbbca", "aadbbbaccc") # False
print s.isInterleave("", "", "") # True
print s.isInterleave("", "1", "") # False
print s.isInterleave("", "1", "1") # True

print time.time()
print s.isInterleave("baababbabbababbaaababbbbbbbbbbbaabaabaaaabaaabbaaabaaaababaabaaabaabbbbaabbaabaabbbbabbbababbaaaabab",
"aababaaabbbababababaabbbababaababbababbbbabbbbbababbbabaaaaabaaabbabbaaabbababbaaaababaababbbbabbbbb",
"babbabbabbababbaaababbbbaababbaabbbbabbbbbaaabbabaababaabaaabaabbbaaaabbabbaaaaabbabbaabaaaabbbbababbbababbabaabababbababaaaaaabbababaaabbaabbbbaaaaabbbaaabbbabbbbaaabaababbaabababbbbababbaaabbbabbbab") # True
print time.time()