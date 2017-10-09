#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ListNode
# Created by yangchao 13/04/2017


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def show(self):
        x = self
        arr = [x.val]
        while x.next is not None:
            x = x.next
            arr.append(x.val)
        print '['+'->'.join([str(i) for i in arr])


head = ListNode(0)
l1 = head

head = ListNode(0)
l2 = head
head.next = ListNode(1)
head = head.next
head.next = ListNode(2)
head = head.next
head.next = ListNode(3)
head = head.next
head.next = ListNode(3)
head = head.next
head.next = ListNode(4)
head = head.next
head.next = ListNode(4)
head = head.next
head.next = ListNode(4)
head = head.next
head.next = ListNode(5)


head = ListNode(0)
l3 = head
head.next = ListNode(0)
head = head.next
head.next = ListNode(1)
head = head.next
head.next = ListNode(1)
head = head.next
head.next = ListNode(2)
head = head.next
head.next = ListNode(3)
head = head.next
head.next = ListNode(4)
head = head.next
head.next = ListNode(4)
head = head.next
head.next = ListNode(5)
head = head.next
head.next = ListNode(5)
head = head.next
