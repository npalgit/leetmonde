#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 127. Word Ladder
# Created by yangchao 01/04/2017

import time
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        wordList.append(beginWord)
        l = len(wordList)
        word_size = len(beginWord)

        mapping = {}
        for i in range(l):
            word = wordList[i]
            for j in range(i+1, l):
                word1 = wordList[j]
                if self.word_differ(word, word1, word_size):
                    mapping[(word, word1)] = 1
                    mapping[(word1, word)] = 1
        last = {(beginWord, beginWord): 0}
        used = {(beginWord, beginWord): 0}
        step = 1
        print time.time(), '1', l
        while 1:
            temp = {}
            step += 1
            for item in last:
                start_word = item[1]
                for i in range(l - 1):
                    word = wordList[i]
                    if (word, start_word) in mapping and (word, start_word) not in used:
                        if word == endWord:
                            return step
                        temp[(start_word, word)] = 0
                        used[(word, start_word)] = 0
                        used[(start_word, word)] = 0
            if len(temp) == 0:
                    return 0
            last = temp

    def word_differ(self, word1, word2, l):
        df = 0
        for i in range(l):
            if word1[i] == word2[i]:
                continue
            if df == 1:
                return False
            df += 1
        return True
s = Solution()

from bigger import big_arr, big_arr2
print time.time()
print s.ladderLength("sand", "acne", big_arr)  # 11
print time.time()

exit()

print s.ladderLength("kiss",
"tusk",
["miss","dusk","kiss","musk","tusk","diss","disk","sang","ties","muss"]) # 5
print s.ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"]) # 5