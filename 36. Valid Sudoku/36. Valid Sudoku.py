#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 36. Valid Sudoku
# Created by yangchao 08/04/2017


class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        mapping = set()
        for line in board:
            mapping.clear()
            for x in line:
                if x in mapping and x != '.':
                    return False
                mapping.add(x)

        for col in range(9):
            mapping.clear()
            for row in range(9):
                if board[row][col] == '.':
                    continue
                if board[row][col] in mapping:
                    return False
                mapping.add(board[row][col])

        for rowx in range(3):
            for coly in range(3):
                mapping.clear()
                for x in range(3):
                    row = 3 * rowx + x
                    for y in range(3):
                        col = 3 * coly + y
                        if board[row][col] == '.':
                            continue
                        if board[row][col] in mapping:
                            return False
                        mapping.add(board[row][col])
        return True