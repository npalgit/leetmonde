#!/usr/bin/env python
# coding=utf-8
import copy


class Hanoi:
    def __init__(self, num):
        self.num = num
        self.package = [
            range(num, 0, -1),
            [],
            []
        ]

    def method1(self):
        self.hanoi1(self.num, 0, 1, 2)

    def hanoi1(self, index, a, b, c):
        if index == 1:
            self.swap(a, c)
        else:
            self.hanoi1(index-1, a, c, b)
            self.swap(a, c)
            self.hanoi1(index-1, b, a, c)

    def swap(self, src, target):
        index = self.package[src].pop()
        self.package[target].append(index)
        print str(index) + ': ' + str(src) + '->' + str(target)


    def hanoi(self, n, a, b, c):
        if n == 1:
            print str(n) + ': ' + a + '->' + c
        else:
            self.hanoi(n-1, a, c, b)
            print str(n) + ': ' + a + '-> ' + c
            self.hanoi(n-1, b, a, c)


    def show_rst(self):
        i = 1
        print '======================'
        for item in self.package:
            print str(i) + ': ' + ','.join(str(a) for a in item)
            i += 1
        print '======================'


if __name__ == '__main__':
    hanoi = Hanoi(4)
    hanoi.show_rst()
    hanoi.method1()
    hanoi.show_rst()
