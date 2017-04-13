#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 98. Validate Binary Search Tree (M)
# Created by yangchao 14/04/2017


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        arr = []
        def _inorder(_root):
            if _root is None:
                return
            _inorder(_root.left)
            arr.append(_root.val)
            _inorder(_root.right)
        _inorder(root)
        if len(arr) < 2:
            return True
        last = arr[0]
        for x in arr[1:]:
            if x <= last:
                return False
            last = x
        return True
