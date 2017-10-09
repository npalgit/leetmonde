#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 19. Remove Nth Node From End of List
# Created by yangchao 28/03/2017
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        hub = head
        saved = hub
        while head is not None:
            n -= 1
            if n < -1:
                hub = hub.next
            head = head.next
        if hub.next is None:
            return None
        if n == 0:
            return saved.next
        hub.next = hub.next.next
        return saved


t = ListNode(1)
head = t
t.next = ListNode(2)
t = t.next
t.next = ListNode(3)

t = t.next
t.next = ListNode(4)

t = t.next
t.next = ListNode(5)

s = Solution()
r = s.removeNthFromEnd(head, 4)
while r is not None:
    print r.val, '=>'
    r = r.next
print '-0--------'
t = ListNode(1)
head = t
t.next = ListNode(2)
r = s.removeNthFromEnd(t, 2)
while r is not None:
    print r.val, '=>'
    r = r.next