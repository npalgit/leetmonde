#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 101. Symmetric Tree (E)
# Created by yangchao 13/04/2017


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root:
            def is_symmetric(t1, t2):
                if t1 is None and t2 is not None:
                    return False
                if t1 is not None and t2 is None:
                    return False
                if t1 is None and t2 is None:
                    return True
                if t1.val != t2.val:
                    return False
                return is_symmetric(t1.left, t2.right) and is_symmetric(t1.right, t2.left)
            return is_symmetric(root.left, root.right)
        else:
            return True
