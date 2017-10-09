#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 71. Simplify Path (M)
# Created by yangchao 10/04/2017


class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        arr = path.split('/')
        ret = []
        for i in arr:
            if i == '.':
                continue
            if i == '..':
                if len(ret) > 0:
                    ret.pop()
            elif i != '':
                ret.append(i)
        return '/' + '/'.join(ret)

s = Solution()
path1 = "/home/"
path2 = "/a/./b/../../c/"

print(s.simplifyPath(''))  # '/'
print(s.simplifyPath('a'))  # '/a'
print(s.simplifyPath('a/a'))  # '/a/a'
print(s.simplifyPath('/'))  # '/'
print(s.simplifyPath('/home'))  # '/home'
print(s.simplifyPath(path1))  # '/home'
print(s.simplifyPath(path2))  # '/c'

