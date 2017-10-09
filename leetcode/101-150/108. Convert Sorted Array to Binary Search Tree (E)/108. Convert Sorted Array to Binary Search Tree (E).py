#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 108. Convert Sorted Array to Binary Search Tree (E)
# Created by yangchao 14/04/2017


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        l = len(nums)
        if l == 0:
            return None
        index = (l-1)/2
        node = TreeNode(nums[index])
        node.left = self.sortedArrayToBST(nums[0: index])
        node.right = self.sortedArrayToBST(nums[index+1: l])
        return node