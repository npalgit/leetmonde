#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 28. Implement strStr()
# Created by yangchao 30/03/2017
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        return self.boyer_moore_way(haystack, needle)

    def bad_letter_way(self, string, pattern):
        length_pattern = len(pattern)
        if length_pattern == 0:
            return 0
        length_string = len(string)
        if length_string == 0:
            return -1
        # 坏字符表
        bad_letter = {}
        i = 0
        for letter in pattern:
            bad_letter[letter] = i
            i += 1
        # 遍历
        i = length_pattern - 1
        while i < length_string:
            string_index = i
            location = length_pattern - 1
            while 1:
                if string[string_index] != pattern[location]:
                    break
                elif location == 0:
                    return string_index
                location -= 1
                string_index -= 1
            if string[string_index] not in bad_letter:
                skip = location + 1
            else:
                skip = location - bad_letter[string[string_index]]
            i += skip
        return -1

    def boyer_moore_way(self, string, pattern):
        length_pattern = len(pattern)
        if length_pattern == 0:
            return 0
        length_string = len(string)
        if length_string == 0:
            return -1
        # 坏字符表
        bad_letter = {}
        i = 0
        for letter in pattern:
            bad_letter[letter] = i
            i += 1
        # 好后缀表
        good_suffix = {}
        suffix = ''
        for i in range(length_pattern - 1, length_pattern / 2 - 1, -1):
            suffix = pattern[i] + suffix
            l = len(suffix)
            found = False
            for j in range(length_pattern - 2, l - 2, -1):
                next_suffix = pattern[j - l + 1:j + 1]
                if suffix == next_suffix:
                    good_suffix[suffix] = length_pattern - j - 1
                    found = True
                    break
            if not found:
                head_suffix_found = False
                k = 1
                while k < l:
                    head_pattern = pattern[0:k]
                    sub_suffix = suffix[l - k:l]
                    if head_pattern == sub_suffix:
                        head_suffix_found = True
                        good_suffix[suffix] = length_pattern - k
                    k += 1
                if not head_suffix_found:
                    good_suffix[suffix] = length_pattern
        # 遍历
        i = length_pattern - 1
        while i < length_string:
            temp_suffix = ''
            string_index = i
            location = length_pattern - 1
            while 1:
                letter_string = string[string_index]
                letter_pattern = pattern[location]
                if letter_string != letter_pattern:
                    break
                elif location == 0:
                    return string_index
                temp_suffix = letter_pattern + temp_suffix
                location -= 1
                string_index -= 1
            if string[string_index] not in bad_letter:
                skip = location + 1
            else:
                skip = location - bad_letter[string[string_index]]
            if location == length_pattern - 1:
                skip1 = 1
            else:
                suffix = pattern[location + 1:length_pattern]
                if suffix not in good_suffix:
                    skip1 = length_pattern
                else:
                    skip1 = good_suffix[suffix]
            if skip1 > skip:
                i += skip1
            else:
                i += skip
        return -1

    def kmp(self, string, pattern):
        pass


s = Solution()
print s.strStr('24b1ab123', 'ab14b11dab1') # -1
print s.strStr('12341234', '3412') # 2
print s.strStr('HERE IS A SIMPLE EXAMPLE', 'EXAMPLE') # 17
print s.strStr('foobarthebarfooman', 'foothebar') # 17
print s.strStr(
    "baabbaaaaaaabbaaaaabbabbababaabbabbbbbabbabbbbbbabababaabbbbbaaabbbbabaababababbbaabbbbaaabbaababbbaabaabbabbaaaabababaaabbabbababbabbaaabbbbabbbbabbabbaabbbaa",
    "bbaaaababa")   # 107