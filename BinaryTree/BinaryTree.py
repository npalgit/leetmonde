#!/usr/bin/env python
# coding=utf-8


class BinaryTree:
    def __init__(self, n):
        self.index = -1
        self.tree = self.create_tree(n)
        self.rst = []

    def create_tree(self, n):
        if n == 0:
            return None
        else:
            self.index += 1
            return {
                'val': self.index,
                'l': self.create_tree(n-1),
                'r': self.create_tree(n-1),
            }

    # 递归版 深度优先 前中后序
    def dfs(self, node):
        if node is None:
            return None
        else:
            #self.rst.append(node['val'])
            self.dfs(node['l'])
            #self.rst.append(node['val'])
            self.dfs(node['r'])
            #self.rst.append(node['val'])

    # 递归版 广度优先
    def bfs(self):
        self.bfs_process([self.tree])

    def bfs_process(self, nodes):
        new_nodes = []
        for item in nodes:
            if item is None:
                continue
            else:
                self.rst.append(item['val'])
                new_nodes.append(item['l'])
                new_nodes.append(item['r'])
        if len(new_nodes) > 0:
            self.bfs_process(new_nodes)
        return True

    # 非递归版
    def no_recursion(self):
        nodes = []
        nodes.append(self.tree)
        while len(nodes) > 0:
            node = nodes.pop()
            if node is None:
                continue
            else:
                self.rst.append(node['val'])
                nodes.append(node['r'])
                nodes.append(node['l'])


    def show_rst(self):
        print ','.join(str(i) for i in self.rst)

if __name__ == '__main__':
    bt = BinaryTree(4)
    #print bt.tree
    #bt.dfs(bt.tree)
    bt.bfs()
    # bt.no_recursion()
    # bt.no_recursion_1()
    bt.show_rst()