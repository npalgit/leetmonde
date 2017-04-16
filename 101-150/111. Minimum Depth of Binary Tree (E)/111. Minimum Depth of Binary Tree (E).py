#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 111. Minimum Depth of Binary Tree (E)
# Created by yangchao 16/04/2017
# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        height = 1
        last = [root]
        _stop = True
        while _stop:
            temp = []
            for x in last:
                if x.left is None and x.right is None:
                    _stop = False
                    break
                if x.left:
                    temp.append(x.left)
                if x.right:
                    temp.append(x.right)
            if _stop:
                height += 1
                last = temp
        return height

s = Solution()

print s.minDepth(None), '0'

print s.minDepth(TreeNode(1)), '1'

tree = TreeNode(1)
tree.left = TreeNode(2)
print s.minDepth(tree), '2'

left = tree.left
left.right = TreeNode(3)
print s.minDepth(tree), '3'
