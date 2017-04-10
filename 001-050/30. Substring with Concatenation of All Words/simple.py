#!/usr/bin/env python
# -*- coding: utf-8 -*-

# simple
# Created by yangchao 31/03/2017

class Solution(object):
    def __init__(self):
        self.all = 0

    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        length_string = len(s)
        length_words = len(words)
        ret = []
        word_size = len(words[0])
        mapping = {}
        for word in words:
            if word in mapping:
                mapping[word] += 1
            else:
                mapping[word] = 1
        for i in range(length_string-length_words*word_size+1):
            next = 0
            curr = {}
            while 1:
                self.all += 1
                next_word = s[next*word_size+i: i+next*word_size+word_size]
                if next_word not in mapping:
                    break
                if next_word in curr:
                    curr[next_word] += 1
                    if mapping[next_word] < curr[next_word]:
                        break
                else:
                    curr[next_word] = 1
                next += 1
            if next == length_words:
                ret.append(i)
                i += word_size-1
        return ret


import time
s = Solution()

print time.time()
print s.findSubstring("abababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababab",
["ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba"])  # [1, 4]
print time.time()
print s.all

print s.findSubstring("mississippi", ["si","is"])  # [1, 4]
print s.findSubstring("ababaab", ["ab","ba","ba"])  # [1]
print s.findSubstring("foobarthebarfooman", ['foo', 'bar', 'the'])  # [6, 0]
print s.findSubstring("wordgoodgoodgoodbestword",["word","good","best","good"])  # 8
print s.findSubstring("foobarfoobar0000foobar", ["foo","bar"])  # [0, 3, 6, 16]
print s.findSubstring("aaa", ["a", "a"])  # [1, 1]

print time.time()
print s.findSubstring("pjzkrkevzztxductzzxmxsvwjkxpvukmfjywwetvfnujhweiybwvvsrfequzkhossmootkmyxgjgfordrpapjuunmqnxxdrqrfgkrsjqbszgiqlcfnrpjlcwdrvbumtotzylshdvccdmsqoadfrpsvnwpizlwszrtyclhgilklydbmfhuywotjmktnwrfvizvnmfvvqfiokkdprznnnjycttprkxpuykhmpchiksyucbmtabiqkisgbhxngmhezrrqvayfsxauampdpxtafniiwfvdufhtwajrbkxtjzqjnfocdhekumttuqwovfjrgulhekcpjszyynadxhnttgmnxkduqmmyhzfnjhducesctufqbumxbamalqudeibljgbspeotkgvddcwgxidaiqcvgwykhbysjzlzfbupkqunuqtraxrlptivshhbihtsigtpipguhbhctcvubnhqipncyxfjebdnjyetnlnvmuxhzsdahkrscewabejifmxombiamxvauuitoltyymsarqcuuoezcbqpdaprxmsrickwpgwpsoplhugbikbkotzrtqkscekkgwjycfnvwfgdzogjzjvpcvixnsqsxacfwndzvrwrycwxrcismdhqapoojegggkocyrdtkzmiekhxoppctytvphjynrhtcvxcobxbcjjivtfjiwmduhzjokkbctweqtigwfhzorjlkpuuliaipbtfldinyetoybvugevwvhhhweejogrghllsouipabfafcxnhukcbtmxzshoyyufjhzadhrelweszbfgwpkzlwxkogyogutscvuhcllphshivnoteztpxsaoaacgxyaztuixhunrowzljqfqrahosheukhahhbiaxqzfmmwcjxountkevsvpbzjnilwpoermxrtlfroqoclexxisrdhvfsindffslyekrzwzqkpeocilatftymodgztjgybtyheqgcpwogdcjlnlesefgvimwbxcbzvaibspdjnrpqtyeilkcspknyylbwndvkffmzuriilxagyerjptbgeqgebiaqnvdubrtxibhvakcyotkfonmseszhczapxdlauexehhaireihxsplgdgmxfvaevrbadbwjbdrkfbbjjkgcztkcbwagtcnrtqryuqixtzhaakjlurnumzyovawrcjiwabuwretmdamfkxrgqgcdgbrdbnugzecbgyxxdqmisaqcyjkqrntxqmdrczxbebemcblftxplafnyoxqimkhcykwamvdsxjezkpgdpvopddptdfbprjustquhlazkjfluxrzopqdstulybnqvyknrchbphcarknnhhovweaqawdyxsqsqahkepluypwrzjegqtdoxfgzdkydeoxvrfhxusrujnmjzqrrlxglcmkiykldbiasnhrjbjekystzilrwkzhontwmehrfsrzfaqrbbxncphbzuuxeteshyrveamjsfiaharkcqxefghgceeixkdgkuboupxnwhnfigpkwnqdvzlydpidcljmflbccarbiegsmweklwngvygbqpescpeichmfidgsjmkvkofvkuehsmkkbocgejoiqcnafvuokelwuqsgkyoekaroptuvekfvmtxtqshcwsztkrzwrpabqrrhnlerxjojemcxel"
,["dhvf","sind","ffsl","yekr","zwzq","kpeo","cila","tfty","modg","ztjg","ybty","heqg","cpwo","gdcj","lnle","sefg","vimw","bxcb"])  # [935]
print time.time()
# [904]
print s.findSubstring("lxiceyvyuodxgsszjyqhoqbmoaevrooclwgrxdrrsvqynixyiqfxijjwjnradgfqelidpzujwmhjxhhfzpehypehfxkifrbkelnvmkejyosvxcdwrhdpxjyejkmodpyiaofnamyyaqwxuzvliychkdltnahtpibsyihyufyuxutsvofepklbnxuczdvqnyiljrldwmawgtoekvizfvauuwxtzuknvuaemohkajgidwmpswqzsqumotipnsekofoatynthtdmqqbkmrjejftxybpovtalypmtpzowuslmimwwgidppwpqzeguxgfyxttmuijraudkicgomjgbhxrgbxcaekabfuoceztgvyqdayumkaorxhaafcclofoubeyffrlardgsdagncwhbehdllhycmmynrwswnfzekfyohhbldkojrtufashphfcabxyqezwpgxfpegahtqrklnrmiadrfhrieralrzaxwhncnpliievtsmhcnktusmfydfjwgluesjgiyuqgylasajunupjodomjwyfcjzjeirojlepksrcsbzhxqsluhzdfxkjjmsnukbfxhxhzomtrncodvbzebejapujbpwxbzdyhaiiquciheymzcmffsofhlpkanibnnbwnjefdipmpqbospuxhkervtbxhjawycsnlytrhifwagmsvirfvwwsrxqajswhuqvirqbaygybpktmvnrslnkencfyvdfrucbnscntlluaxpmsegkrvxwibdgwgoqcsrpnwcghpcjntxhadurzrpjsssrzghdaavnwxvdpzoctmjtpdmqwcapwuixapbcrwqovltkniogwybldpeatgrqazpcqsehowxmiryxbndxngkqxqqrwhjwiyayrfghbfvlyuizjnywvlmtbfmymxwvxxvqedafjvthrbjarhwmslhwqvwessbqrxivaidjewtvzcyqlwfghmcxiyccsdukcdhdlkorghnilnyxjdfrshqahuebazlccvfpfwhofwwrjwqsavjsecunwyowzazdxgteecskyqbhntbponhupdhldvkdxjgurbzwdtgbmjkzcmqszxmqcvbfsliqwrmqunmyjubvfowhambblprnkuucifueyjwswisheucjiaskotnzieoualxiqtpoclibwbiaxnmhnercagdkkufmfevxzmncxvdtynwvaicoovsqbxbntiaaoxxnjmpgiucgiaeikgyyesrfquvjcvmsujfdwxlgrpmbpsmzzkaffrkxlfipcuhweobclnifcwguputqftvmmhjzprotmxssmtuxieencnhthcjoygakojkfbaypyqhmmdjwjojlbqfkvqztzzdpjpumsubsnkezpnvydhlgzqrujsnirtzaktoeprwcdadsqbsvieehwxefptpgoojzjxdzrcbucfpsihoqluzkrfpgzhmnxxohxuiowlkyqztajjqwdsguxyayfooemcnjwvzuhjvzloauxsqckxw",
["gbmjkzcmqszxmqcvbfsliqw","obclnifcwguputqftvmmhjz","iaxnmhnercagdkkufmfevxz","oygakojkfbaypyqhmmdjwjo","kuucifueyjwswisheucjias","ponhupdhldvkdxjgurbzwdt","fptpgoojzjxdzrcbucfpsih","kotnzieoualxiqtpoclibwb","lkyqztajjqwdsguxyayfooe","ghmcxiyccsdukcdhdlkorgh","yesrfquvjcvmsujfdwxlgrp","wyowzazdxgteecskyqbhntb","mbpsmzzkaffrkxlfipcuhwe","oqluzkrfpgzhmnxxohxuiow","mncxvdtynwvaicoovsqbxbn","ktoeprwcdadsqbsvieehwxe","protmxssmtuxieencnhthcj","dafjvthrbjarhwmslhwqvwe","kezpnvydhlgzqrujsnirtza","rmqunmyjubvfowhambblprn","izjnywvlmtbfmymxwvxxvqe","nilnyxjdfrshqahuebazlcc","tiaaoxxnjmpgiucgiaeikgy","ssbqrxivaidjewtvzcyqlwf","vfpfwhofwwrjwqsavjsecun","jlbqfkvqztzzdpjpumsubsn"])  # [935]
print time.time()