#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 100. Same Tree
# Created by yangchao 06/04/2017
# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p is None and q is None:
            return True
        elif p is not None and q is not None:
            if p.val != q.val:
                return False
        elif p is None and q is not None:
            return False
        elif p is not None and q is None:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)