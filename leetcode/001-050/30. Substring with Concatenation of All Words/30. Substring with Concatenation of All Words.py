#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 30. Substring with Concatenation of All Words
# Created by yangchao 30/03/2017

class Solution(object):
    def __init__(self):
        self.all = []

    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        left = len(words)
        length_string = len(s)
        self.all = []
        mapping = {}
        for word in words:
            if word in mapping:
                mapping[word] += 1
            else:
                mapping[word] = 1
        self.generateStrings(mapping, '', left)
        result = []
        for i in self.all:
            index = s.find(i)
            if index < 0:
                continue
            result.append(index)
            len_word = len(i)

            last = 0
            next = s[index + 1:]
            while index >= 0 and length_string - index >= len_word:
                last += index + 1
                index = next.find(i)
                if index > -1:
                    result.append(index+last)
                next = next[index+1:]

        return result

    def generateStrings(self, unused, now, left):
        if left == 0:
            self.all.append(now)
        for i in unused:
            if unused[i] <= 0:
                continue
            unused[i] -= 1
            self.generateStrings(unused, now+i, left-1)
            unused[i] += 1

s = Solution()
print s.findSubstring("mississippi", ["si","is"])  # [1, 4]
print s.findSubstring("ababaab", ["ab","ba","ba"])  # [1]
print s.findSubstring("foobarthebarfooman", ['foo', 'bar', 'the'])  # [6, 0]
print s.findSubstring("wordgoodgoodgoodbestword",["word","good","best","good"])  # 8
print s.findSubstring("foobarfoobar0000foobar", ["foo","bar"])  # [0, 3, 6, 16]
print s.findSubstring("aaa", ["a", "a"])  # [1, 1]
import time
print time.time()
print s.findSubstring("pjzkrkevzztxductzzxmxsvwjkxpvukmfjywwetvfnujhweiybwvvsrfequzkhossmootkmyxgjgfordrpapjuunmqnxxdrqrfgkrsjqbszgiqlcfnrpjlcwdrvbumtotzylshdvccdmsqoadfrpsvnwpizlwszrtyclhgilklydbmfhuywotjmktnwrfvizvnmfvvqfiokkdprznnnjycttprkxpuykhmpchiksyucbmtabiqkisgbhxngmhezrrqvayfsxauampdpxtafniiwfvdufhtwajrbkxtjzqjnfocdhekumttuqwovfjrgulhekcpjszyynadxhnttgmnxkduqmmyhzfnjhducesctufqbumxbamalqudeibljgbspeotkgvddcwgxidaiqcvgwykhbysjzlzfbupkqunuqtraxrlptivshhbihtsigtpipguhbhctcvubnhqipncyxfjebdnjyetnlnvmuxhzsdahkrscewabejifmxombiamxvauuitoltyymsarqcuuoezcbqpdaprxmsrickwpgwpsoplhugbikbkotzrtqkscekkgwjycfnvwfgdzogjzjvpcvixnsqsxacfwndzvrwrycwxrcismdhqapoojegggkocyrdtkzmiekhxoppctytvphjynrhtcvxcobxbcjjivtfjiwmduhzjokkbctweqtigwfhzorjlkpuuliaipbtfldinyetoybvugevwvhhhweejogrghllsouipabfafcxnhukcbtmxzshoyyufjhzadhrelweszbfgwpkzlwxkogyogutscvuhcllphshivnoteztpxsaoaacgxyaztuixhunrowzljqfqrahosheukhahhbiaxqzfmmwcjxountkevsvpbzjnilwpoermxrtlfroqoclexxisrdhvfsindffslyekrzwzqkpeocilatftymodgztjgybtyheqgcpwogdcjlnlesefgvimwbxcbzvaibspdjnrpqtyeilkcspknyylbwndvkffmzuriilxagyerjptbgeqgebiaqnvdubrtxibhvakcyotkfonmseszhczapxdlauexehhaireihxsplgdgmxfvaevrbadbwjbdrkfbbjjkgcztkcbwagtcnrtqryuqixtzhaakjlurnumzyovawrcjiwabuwretmdamfkxrgqgcdgbrdbnugzecbgyxxdqmisaqcyjkqrntxqmdrczxbebemcblftxplafnyoxqimkhcykwamvdsxjezkpgdpvopddptdfbprjustquhlazkjfluxrzopqdstulybnqvyknrchbphcarknnhhovweaqawdyxsqsqahkepluypwrzjegqtdoxfgzdkydeoxvrfhxusrujnmjzqrrlxglcmkiykldbiasnhrjbjekystzilrwkzhontwmehrfsrzfaqrbbxncphbzuuxeteshyrveamjsfiaharkcqxefghgceeixkdgkuboupxnwhnfigpkwnqdvzlydpidcljmflbccarbiegsmweklwngvygbqpescpeichmfidgsjmkvkofvkuehsmkkbocgejoiqcnafvuokelwuqsgkyoekaroptuvekfvmtxtqshcwsztkrzwrpabqrrhnlerxjojemcxel"
,["dhvf","sind","ffsl","yekr","zwzq","kpeo","cila","tfty","modg","ztjg","ybty","heqg","cpwo","gdcj","lnle","sefg","vimw","bxcb"])  # [1, 1]
print time.time()