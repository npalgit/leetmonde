#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 110. Balanced Binary Tree (E)
# Created by yangchao 16/04/2017


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def max_min_height(_root):
            if _root is None:
                return True, 0
            if _root.left is None and _root.right is None:
                return True, 1
            left = max_min_height(_root.left)
            right = max_min_height(_root.right)
            if left[0] and right[0]:
                _a = left[1] - right[1]
                if _a > 1 or _a < -1:
                    return False, 0
                elif _a > 0:
                    return True, left[1] + 1
                return True, right[1] + 1
            return False, 0
        return max_min_height(root)[0]


s = Solution()

print s.isBalanced(TreeNode(1))