#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 113. Path Sum II (M)
# Created by yangchao 16/04/2017


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def __init__(self):
        self.ret = []

    def pathSum(self, root, sum, path=[]):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root:
            return False

        sum -= root.val
        new_path = path+[root.val]
        if sum == 0 and root.left is None and root.right is None:
            self.ret.append(new_path)
        self.pathSum(root.left, sum, new_path)
        self.pathSum(root.right, sum, new_path)
