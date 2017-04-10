#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 没有做出来
# 99. Recover Binary Search Tree
# Created by yangchao 07/04/2017
# Definition for a binary tree node.


class Solution(object):
    def __init__(self):
        self.mistake1 = None
        self.mistake2 = None
        self.parent = None

    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        pass

s = Solution()

from tree import t1, t2

s.recoverTree(t1)
t1.show()
s.recoverTree(t2)
t2.show()

