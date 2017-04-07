#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 129. Sum Root to Leaf Numbers
# Created by yangchao 28/03/2017

# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def __init__(self):
        self.sum = 0
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        self.process(0, root)
        return self.sum

    def process(self, temp, node):
        tmp_sum = 10*temp + node.val
        if node.left is not None:
            self.process(tmp_sum, node.left)
        if node.right is not None:
            self.process(tmp_sum, node.right)
        if node.left is None and node.right is None:
            self.sum += tmp_sum



s = Solution()

l = TreeNode(2)
r = TreeNode(3)
root = TreeNode(1)
root.left = l
root.right = r

print(s.sumNumbers(root))  # 25