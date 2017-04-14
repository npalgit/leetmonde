#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 105. Construct Binary Tree from Preorder and Inorder Traversal (M)
# Created by yangchao 14/04/2017
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def show(self, _root):
        if _root is None:
            return
        print _root.val
        self.show(_root.left)
        self.show(_root.right)


class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        m = len(preorder)
        n = len(inorder)
        if m != n or m == 0:
            return None

        node1 = TreeNode(preorder[0])
        root = preorder[0]
        index = inorder.index(root)
        node1.left = self.buildTree(preorder[1:index+1], inorder[:index])
        node1.right = self.buildTree(preorder[index+1:], inorder[index+1:])
        return node1



s = Solution()

r = s.buildTree([4, 6, 1, 3, 2, 8, 7, 6], [1, 3, 6, 2, 4, 6, 7, 8])
r.show(r)