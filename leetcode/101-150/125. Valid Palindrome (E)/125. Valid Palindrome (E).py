#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 125. Valid Palindrome (E)
# Created by yangchao 16/04/2017


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.encode('utf-8')
        l = len(s)
        if l == 0:
            return True
        s = str.lower(s)
        b = 0
        e = l - 1

        letters = 'abcdefghijklmnopqrstuvwxyz0123456789'
        while b <= e:
            if s[b] not in letters:
                b += 1
                continue
            if s[e] not in letters:
                e -= 1
                continue
            s1 = s[b]
            s2 = s[e]
            if s[b] != s[e]:
                return False
            b += 1
            e -= 1
        return True


s = Solution()
print s.isPalindrome(''), 'True'
print s.isPalindrome('0p'), 'False'
print s.isPalindrome(".G?j!:;;:Gj?!."), 'False'
print s.isPalindrome("race a car"), 'False'
print s.isPalindrome('A man, a plan, a canal: Panama'), 'True'
