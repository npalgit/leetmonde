#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 94. Binary Tree Inorder Traversal (M)
# Created by yangchao 13/04/2017


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ret = []

        def _inorder(root):
            if root is None:
                return
            _inorder(root.left)
            ret.append(root.val)
            _inorder(root.right)
        _inorder(root)
        return ret
