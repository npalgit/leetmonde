#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 87. Scramble String
# Created by yangchao 06/04/2017


class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if s1 == s2:
            return True
        l1 = len(s1)
        if l1 != len(s2):
            return False
        mapping = {chr(x): 0 for x in range(97, 123)}
        for i in s1:
            mapping[i] += 1
        for letter in s2:
            if letter in mapping and mapping[letter] > 0:
                mapping[letter] -= 1
            else:
                return False

        for i in range(1, l1):
            r1 = self.isScramble(s1[:i], s2[:i])
            r2 = self.isScramble(s1[i:], s2[i:])
            if r1 and r2:
                return True

            r1 = self.isScramble(s1[:i], s2[l1-i:])
            r2 = self.isScramble(s1[i:], s2[:l1-i])
            if r1 and r2:
                return True
        return False

s = Solution()
print s.isScramble("great", "tgrea")  # True
print s.isScramble('', '')  # True
print s.isScramble('', 'a')  # False
print s.isScramble('a', 'a')  # True
print s.isScramble('ba', 'ab')  # True