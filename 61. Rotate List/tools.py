#!/usr/bin/env python
# -*- coding: utf-8 -*-

# tools
# Created by yangchao 09/04/2017


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def show(self):
        a = self
        print self.val, '----------'
        while a.next:
            print a.val, '->'
            a = a.next

        print a.val, '->'

t = ListNode(1)
head = t
saved = head
for i in range(2, 6):
    t.next = ListNode(i)
    t = t.next

head1 = ListNode(1)

