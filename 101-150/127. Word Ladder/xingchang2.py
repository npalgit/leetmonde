#!/usr/bin/env python
# -*- coding: utf-8 -*-

# xingchang2
# Created by yangchao 02/04/2017
import time
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        # 首先把wordlist进行扩充
        word_length = len(beginWord)
        wordList.append(beginWord)
        # 首先构建每个word与之相连的word
        dict = {}
        for word in wordList:
            # 为当前的word构建的word构建一个与之相连的临接字典
            dict[word] = []
        # 填充临接字典
        for word in wordList:
            src_word = list(word)
            new_word = list(word)
            for index in range(0, word_length):
                if index > 0:
                    new_word[index-1] = src_word[index-1]
                for letter in 'abcdefghijklmnopqrstuvwxyz':
                    # 字母替换
                    new_word[index] = letter
                    tmp_word = ''.join(new_word)
                    if tmp_word in dict:
                        dict[word].append(tmp_word)
        print time.time(), 1
        # 广度优先遍历
        sets = {}
        for item in dict[beginWord]:
            sets[item] = 1
        dict.pop(beginWord)
        layer = 1
        while len(sets) != 0:
            layer += 1
            new_set = {}
            if endWord in sets:
                return layer
            for item in sets:
                if item in dict:
                    link = dict[item]
                    for tmp in link:
                        if tmp in dict:
                            new_set[tmp] = 1
                    dict.pop(item)
            sets = new_set
        return 0

s = Solution()
from bigger import big_arr, big_arr2
print time.time()
print s.ladderLength("sand", "acne", big_arr)  # 11
print time.time()
exit()