#!/usr/bin/env python
# -*- coding: utf-8 -*-

# bset
# Created by yangchao 02/04/2017
from collections import defaultdict
class Solution(object):
    def ladderLength(self, start, end, wordList):
        wordLen = len(start)
        front, back = defaultdict(list), defaultdict(list)
        front[start].append([start])
        back[end].append([end])
        # remove start from dict, add end to dict if it is not there
        dict = set(wordList)

        forward, result = True, []
        while front:
            # get all valid transformations
            nextSet = defaultdict(list)
            for word, paths in front.items():
                for index in range(wordLen):
                    for ch in 'abcdefghijklmnopqrstuvwxyz':
                        nextWord = word[:index] + ch + word[index+1:]
                        if nextWord in dict:
                            # update paths
                            if forward:
                                # append next word to path
                                nextSet[nextWord].extend([path + [nextWord] for path in paths])
                            else:
                                # add next word in front of path
                                nextSet[nextWord].extend([[nextWord] + path for path in paths])
            front = nextSet
            common = set(front) & set(back)
            if common:
                # path is through
                if not forward:
                    # switch front and back if we were searching backward
                    front, back = back, front
                result.extend([head + tail[1:] for word in common for head in front[word] for tail in back[word]])
                return result

            if len(front) > len(back):
                # swap front and back for better performance (smaller nextSet)
                front, back, forward = back, front, not forward

            # remove transformations from wordDict to avoid cycles
            dict -= set(front)

        return []
s = Solution()
import time
from bigger import big_arr, big_arr2
print time.time()
print s.ladderLength("sand", "acne", big_arr)  # 11, 10ms
print time.time()
exit()