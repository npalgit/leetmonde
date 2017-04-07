#!/usr/bin/env python
# coding=utf-8
import copy


# 递归版八皇后
class EightQueens:
    def __init__(self, dim):
        self.dim = dim
        arr = [0 for i in range(0, dim)]
        self.tree = [copy.deepcopy(arr) for i in range(0, dim)]

        self.index = 0

    def process(self, row, col, tree):
        position = {'row': row, 'col': col}
        tree[position['row']][position['col']] = 1
        row += 1
        position['row'] = row
        if row >= self.dim:
            self.show(tree)
            return True
        for i in range(0, self.dim):
            position['col'] = i
            if not self._check(position, tree):
                continue
            self.process(row, i, copy.deepcopy(tree))

    def _check(self, position, tree):
        y = position['row']
        x = position['col']
        for i in range(0, self.dim):
            if tree[y][i] == 1:
                return False
            if tree[i][x] == 1:
                return False
            tx = x - i
            ty = y - i
            if tx > -1 and ty > -1:
                if tree[ty][tx] == 1:
                    return False
            tx = x + i
            ty = y - i
            if tx < self.dim and ty > -1:
                if tree[ty][tx] == 1:
                    return False
            tx = x - i
            ty = y + i
            if tx < self.dim and ty < self.dim:
                if tree[ty][tx] == 1:
                    return False
            tx = x + i
            ty = y + i
            if tx < self.dim and ty < self.dim:
                if tree[ty][tx] == 1:
                    return False
        return True

    def main(self):
        for i in range(0, self.dim):
            self.process(0, i, copy.deepcopy(self.tree))

    def show(self, tree):
        i = 0
        print '>>>>' + str(self.index) + ':=================================='
        for arr in tree:
            _str = str(i) + ': ' + ' '.join([str(num) for num in arr])
            i += 1
            print _str
        self.index += 1


eq = EightQueens(5)
eq.main()
