#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 124. Binary Tree Maximum Path Sum (H)
# Created by yangchao 17/04/2017


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def __init__(self):
        self.ret = 0

    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        self.ret = root.val
        self.single_path(root)
        return self.ret

    def single_path(self, _root):
        """
        返回该节点一条最大单路径
        更新该节点的最大值
        :param _root:
        :return: 大于等于0
        """
        if _root is None:
            return 0

        length1 = self.single_path(_root.left)
        length2 = self.single_path(_root.right)

        if _root.val < 0:
            if length1 < 0 and length2 < 0:
                temp = max([length1, length2, _root.val])
                if temp > self.ret:
                    self.ret = temp
                return _root.val

            if length1 >= 0 and length2 >= 0:
                _max = length1
                if length2 > length1:
                    _max = length2
                _sum = length1 + length2 + _root.val
                if _sum > self.ret:
                    self.ret = _sum
                return _max + _root.val
            if length1 >= 0:
                return length1 + _root.val
            return length2 + _root.val
        else:
            if length1 >= 0 and length2 >= 0:
                _sum = length1 + length2 + _root.val
                if _sum > self.ret:
                    self.ret = _sum
                if length1 > length2:
                    return length1 + _root.val
                return length2 + _root.val
            if length1 < 0 and length2 < 0:
                if _root.val > self.ret:
                    self.ret = _root.val
                return _root.val
            if length1 >= 0:
                _sum = _root.val + length1
                if _sum > self.ret:
                    self.ret = _sum
                return _sum
            _sum = _root.val + length2
            if _sum > self.ret:
                self.ret = _sum
            return _sum



s = Solution()

t = TreeNode(-1)
t.left = TreeNode(8)
t.right = TreeNode(2)
print s.maxPathSum(t), 9

t = TreeNode(-3)
print s.maxPathSum(t), -3

t = TreeNode(8)
t.left = TreeNode(9)
t.right = TreeNode(-6)
t.right.left = TreeNode(5)
t.right.right = TreeNode(9)
print s.maxPathSum(t), 20

t = TreeNode(1)
t.left = TreeNode(2)
t.left.left = TreeNode(3)
t.left.left.left = TreeNode(4)
t.left.left.left.left = TreeNode(5)
print s.maxPathSum(t), 15

