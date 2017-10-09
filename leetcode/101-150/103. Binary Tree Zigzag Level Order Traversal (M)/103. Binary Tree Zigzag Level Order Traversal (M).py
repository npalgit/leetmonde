#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 103. Binary Tree Zigzag Level Order Traversal (M)
# Created by yangchao 14/04/2017
# 仿佛在逗我笑


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ret = []
        last = [root]
        inorder = True
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
                if not inorder:
                    temp.reverse()
                inorder = not inorder
                ret.append(temp)
            last = temp_last
        return ret

