#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 68. Text Justification
# Created by yangchao 06/04/2017


class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        l = len(words)
        if l == 0:
            return [
                ''.join(' ' for i in range(maxWidth))
            ]
        i = 0

        result = []
        length = 0
        temp_arr = []
        while i < l:
            if length + len(words[i]) > maxWidth:
                words_num = len(temp_arr)
                space_length = maxWidth - length + words_num
                if words_num > 1:
                    temp = []
                    space_num = space_length / (words_num - 1)
                    temp_space = ''.join([' ' for x in range(space_num)])
                    pre_space_num = space_length % (words_num - 1)

                    for j in range(words_num-1):
                        temp.append(temp_arr[j])
                        temp.append(temp_space)
                        if j < pre_space_num:
                            temp.append(' ')
                    temp.append(temp_arr[words_num - 1])
                    result.append(''.join(temp))
                else:
                    space_length = maxWidth - length + 1
                    temp_arr.append(''.join([' ' for x in range(space_length)]))
                    result.append(''.join(temp_arr))
                length = 0
                temp_arr = []
            else:
                temp_arr.append(words[i])
                length += len(words[i]) + 1
                i += 1

        space_length = maxWidth - length + 1
        temp = []
        for index, word in enumerate(temp_arr):
            if index == len(temp_arr) - 1:
                break
            temp.append(word)
            temp.append(' ')
        temp.append(temp_arr[len(temp_arr) - 1])
        temp.append(''.join([' ' for x in range(space_length)]))
        result.append(''.join(temp))
        return result


s = Solution()

print s.fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16)   # [" "]
print s.fullJustify([" "], 16)   # [" "]
print s.fullJustify([], 1)   # [" "]
print s.fullJustify([""], 1)   # [" "]
print s.fullJustify([" "], 1)   # [" "]
print s.fullJustify(["123", "123", "123", "1"], 7)   # [" "]
