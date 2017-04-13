#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 104. Maximum Depth of Binary Tree (E)
# Created by yangchao 13/04/2017


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ret = [0]  # 简单变量传不进去, 好奇怪好奇怪

        def _max_depth(_root, _depth=0):
            if _root is None:
                return
            _depth += 1
            if _depth > ret[0]:
                ret[0] = _depth
            _max_depth(_root.left, _depth)
            _max_depth(_root.right, _depth)
        _max_depth(root)
        return ret[0]
