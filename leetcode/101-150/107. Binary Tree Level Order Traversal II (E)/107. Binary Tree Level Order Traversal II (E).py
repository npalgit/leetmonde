#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 107. Binary Tree Level Order Traversal II (E)
# Created by yangchao 14/04/2017


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ret = []
        last = [root]
        while last:
            temp = []
            temp_last = []
            for node in last:
                if node is None:
                    continue
                temp.append(node.val)
                temp_last.append(node.left)
                temp_last.append(node.right)
            if temp:
                ret.append(temp)
            last = temp_last
        ret.reverse()
        return ret
