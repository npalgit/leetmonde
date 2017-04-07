#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 32. Longest Valid Parentheses
# Created by yangchao 30/03/2017
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_result = 0
        temp_result = 0
        count = 0      # 分数
        last = []
        index = 0
        for i in s:
            if i == '(':
                val = 1
                last.append(index)
            else:
                if count > 0:
                    last.pop()
                    l = len(last)
                    if len(last) > 0:
                        last_one = last[l-1]
                    else:
                        last_one = -1
                    temp = index - last_one
                    if temp > max_result:
                        max_result = temp
                else:
                    last.append(index)
                val = -1
            index += 1
            count += val
            if count < 0:
                if temp_result > max_result:
                    max_result = temp_result
                temp_result = 0
                count = 0
            else:
                temp_result += 1
        last_one = 0
        if count > 0:
            last_one = last.pop()
        if temp_result-count-last_one > max_result:
            max_result = temp_result-count-last_one
        return max_result

s = Solution()
print s.longestValidParentheses("(())()(((")   # 10
print s.longestValidParentheses(")()(((())))(")   # 10
print s.longestValidParentheses(")(((((()())()()))()(()))(")   # 22
print s.longestValidParentheses('()(()()()')   # 6
print s.longestValidParentheses(')()')   # 2
print s.longestValidParentheses('(()')   # 2
print s.longestValidParentheses('()(()))')   # 6
print s.longestValidParentheses('()(()))()')   # 6
print s.longestValidParentheses('()()()(()')   # 6
