#!/usr/bin/env python
# coding=utf-8
import copy


class Arrangement:
    def __init__(self, order):
        self.num = order+1
        self.rst = []

    # 深度优先 递归
    def method1(self, index, arr):
        if index == self.num-1:
            self.rst.append(arr)
            return True
        for i in range(1, self.num):
            new_arr = copy.deepcopy(arr)
            if i in new_arr:
                continue
            else:
                new_arr.append(i)
                self.method1(index+1, new_arr)

    def method2(self, all_num=[], used_arr=[], _list=[]):
        '''
        深度 遍历
        :param all_num:
        :param used_arr:
        :param _list:
        :return:
        '''
        if len(all_num) == len(used_arr):
            self.rst.append(_list)
            return
        for item in all_num:
            new_list = copy.deepcopy(_list)
            new_used_arr = copy.deepcopy(used_arr)
            if item in used_arr:
                continue
            l = len(new_list) + 1
            if l % item == 0 or item % l == 0:
                new_used_arr.append(item)
                new_list.append(item)
                self.method2(all_num, new_used_arr, new_list)


    def show_rst(self):
        index = 1
        for item in self.rst:
            print str(index) + ': ' + ','.join([str(i) for i in item])
            index += 1


if __name__ == '__main__':
    a1 = Arrangement(4)
    #a1.method1(0, [])
    a1.method2([1, 2, 3, 4])

    a1.show_rst()

