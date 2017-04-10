#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 25. Reverse Nodes in k-Group
# Created by yangchao 28/03/2017
# Definition for singly-linked list.
import copy
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseKGroup(self, head, n):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        count = 0
        tmp_node = head
        while tmp_node is not None:
            count += 1
            tmp_node = tmp_node.next
        if n < 2 or n > count:
            return head
        if head is None or head.next is None:
            return head
        i = 0
        saved = head
        tmp_node = None
        while i < n and head is not None:
            i += 1
            hub = head
            head = head.next
            hub.next = tmp_node
            tmp_node = hub

        saved.next = self.reverseKGroup(head, n)
        return hub

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
l.next = ListNode(7)
l = l.next
l.next = ListNode(8)
l = l.next
l.next = ListNode(9)
l = l.next
l.next = ListNode(10)
l = l.next
l.next = ListNode(11)
l = l.next

s = Solution()
r = s.reverseKGroup(copy.deepcopy(head), 3)
while r is not None:
    print r.val, "->"
    r = r.next
print '-------------'

s = Solution()
r = s.reverseKGroup(copy.deepcopy(head), 2)
while r is not None:
    print r.val, "->"
    r = r.next
print '-------------'

s = Solution()
r = s.reverseKGroup(copy.deepcopy(head), 5)
while r is not None:
    print r.val, "->"
    r = r.next
