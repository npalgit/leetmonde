#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 89. Gray Code (M)
# Created by yangchao 14/04/2017
"""
此方法从对应的n位二进制码字中直接得到n位格雷码码字，步骤如下：
对n位二进制的码字，从右到左，以0到n-1编号
如果二进制码字的第i位和i+1位相同，则对应的格雷码的第i位为0，否则为1（当i+1=n时，二进制码字的第n位被认为是0，即第n-1位不变）[3]
"""


class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n == 0:
            return [0]
        ret = []
        l = 2**n
        for i in range(l):
            bin_num = bin(i)[2:]
            bin_arr = ['0' for x in range(n-len(bin_num)+1)]
            bin_arr.append(bin_num)
            num = ''.join(bin_arr)
            gray = []
            for j in range(n):
                if num[j] == num[j+1]:
                    gray.append('0')
                else:
                    gray.append('1')
            ret.append(int(''.join(gray), 2))
        return ret

s = Solution()
print s.grayCode(0), '[0]'
print s.grayCode(2), '[0, 1, 3, 2]'
print s.grayCode(5)
print '[0, 1, 3, 2, 6, 7, 5, 4, 12, 13, 15, 14, 10, 11, 9, 8, 24, 25, 27, 26, 30, 31, 29, 28, 20, 21, 23, 22, 18, 19, 17, 16]'



