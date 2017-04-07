#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 21. Merge Two Sorted Lists
# Created by yangchao 28/03/2017
# Definition for singly-linked list.

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def __init__(self):
        self.result = None
        self.saved = ListNode(0)
        
    def generateNode(self, val):
        if self.result is None:
            self.result = ListNode(val)
            self.saved.next = self.result
        else:
            self.result.next = ListNode(val)
            self.result = self.result.next
    
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        r = None
        while l1 is not None or l2 is not None:
            if l1 is None:
                self.generateNode(l2.val)
                l2 = l2.next
                continue
            if l2 is None or l1.val < l2.val:
                self.generateNode(l1.val)
                l1 = l1.next
                continue
            self.generateNode(l2.val)
            l2 = l2.next

        return self.saved.next

l1 = ListNode(1)
head1 = l1
l1.next = ListNode(1)
l1 = l1.next
l1.next = ListNode(2)
l1 = l1.next
l1.next = ListNode(2)
l1 = l1.next
l1.next = ListNode(3)
l1 = l1.next

l2 = ListNode(2)
head2 = l2
l2.next = ListNode(2)
l2 = l2.next
l2.next = ListNode(2)
l2 = l2.next
l2.next = ListNode(3)
l2 = l2.next
l2.next = ListNode(3)
l2 = l2.next

s = Solution()
r = s.mergeTwoLists(head1, head2)
while r is not None:
    print r.val, '->'
    r = r.next
