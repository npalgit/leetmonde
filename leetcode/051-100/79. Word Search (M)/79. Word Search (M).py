#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 79. Word Search (M)
# Created by yangchao 11/04/2017


class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        m = len(board)
        if m == 0:
            return False
        n = len(board[0])
        if n == 0:
            return False
        mapping = {}
        word_size = len(word)
        if word_size == 0:
            return True
        for row, line in enumerate(board):
            for col, letter in enumerate(line):
                if letter not in mapping:
                    mapping[letter] = set()
                mapping[letter].add((row, col))

        def _dfs(index, route, last_loc):
            if index == word_size:
                return True
            _letter = word[index]
            if _letter not in mapping:
                return False
            if last_loc:
                temp = set()
                temp.add(last_loc)
                route = route | temp
            locs = mapping[_letter] - route
            found = False
            if locs:
                for x in locs:
                    if last_loc:
                        if x[0] == last_loc[0]:
                            if x[1] == last_loc[1] - 1 or x[1] == last_loc[1] + 1:
                                if _dfs(index + 1, route, x):
                                    found = True
                        elif x[1] == last_loc[1]:
                            if x[0] == last_loc[0] - 1 or x[0] == last_loc[0] + 1:
                                if _dfs(index + 1, route, x):
                                    found = True
                    else:
                        if _dfs(index + 1, route, x):
                            return True
            return found

        return _dfs(0, set(), None)

s = Solution()

print s.exist([], 'a')   # False
print s.exist([], '')   # False
print s.exist([[]], '')   # False

print s.exist([['a', 'b'], ['c', 'd']], 'ac')  # true
print s.exist([['a', 'b'], ['c', 'd']], 'acd')  # true
print s.exist([['a', 'b'], ['c', 'd']], 'abd')  # true
print s.exist([['a', 'b'], ['c', 'd']], 'abd')  # true
print s.exist([['a']], 'ab')  # False
print s.exist([['aa']], 'aaa')  # False
