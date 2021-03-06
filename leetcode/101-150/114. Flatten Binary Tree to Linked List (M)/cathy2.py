#!/usr/bin/env python
# -*- coding: utf-8 -*-

# cathy2
# Created by yangchao 16/04/2017


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def show(self, x):
        """
        打印结果
        :param x:
        :return:
        """
        while x:
            print x.val
            x = x.right
        print '------'

    def __init__(self):
        self.new_tree = None

    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if root is None:
            pass
        else:
            # tree的先序遍历
            self.new_tree = TreeNode(root.val)
            saved = self.new_tree
            p = self.new_tree
            self.process(root.left, p)
            self.process(root.right, p)

            root.val = self.new_tree.val
            root.left = None
            root.right = saved.right

    def process(self, root, p):
        """
        :param root: 当前的结点
        :param p: 新树的根节点
        :return:
        """
        if root is None:
            return
        p.right = TreeNode(root.val)
        p = p.right
        self.process(root.left, p)
        self.process(root.right, p)







s = Solution()

# 123456
tree = TreeNode(1)
tree.left = TreeNode(2)
tree.left.left = TreeNode(3)
tree.left.right = TreeNode(4)

tree.right = TreeNode(5)
tree.right.right = TreeNode(6)

s.flatten(tree)



tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(3)

left = tree.left
left.left = TreeNode(4)
left.right = TreeNode(5)
left.right.right = TreeNode(9)

left = left.left
left.left = TreeNode(8)

left = left.left
left.right = TreeNode(6)

right = left.right
right.left = TreeNode(5)
right.right = TreeNode(4)

right = tree.right
right.left = TreeNode(6)
right.right = TreeNode(7)
s.flatten(tree)


head = TreeNode(1)
a = TreeNode(2)
head.left = a
test = Solution()
m = test.flatten(head)