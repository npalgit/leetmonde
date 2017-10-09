#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 24. Swap Nodes in Pairs
# Created by yangchao 28/03/2017
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        next = head.next
        head.next = self.swapPairs(next.next)
        next.next = head
        return next
l = ListNode(1)
head = l
l.next = ListNode(2)
l = l.next
l.next = ListNode(3)
l = l.next
l.next = ListNode(4)
l = l.next
l.next = ListNode(5)
l = l.next
l.next = ListNode(6)
l = l.next

s = Solution()
r = s.swapPairs(head)
while r is not None:
    print r.val, "->"
    r = r.next
