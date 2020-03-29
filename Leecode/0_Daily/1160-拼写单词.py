# -*- coding: utf-8 -*-
# @Author: klaus
# @Date:   2020-03-17 09:07:44
# @Last Modified by:   sniky-lyu
# @Last Modified time: 2020-03-28 11:03:00

'''{1160. 拼写单词}
给你一份『词汇表』（字符串数组） words 和一张『字母表』（字符串） chars。
假如你可以用 chars 中的『字母』（字符）拼写出 words 中的某个『单词』（字符串），那么我们就认为你掌握了这个单词。
注意：每次拼写时，chars 中的每个字母都只能用一次。
      返回词汇表 words 中你掌握的所有单词的 长度之和。
示例 1：
    输入：words = ["cat","bt","hat","tree"], chars = "atach"
    输出：6
    解释：
    可以形成字符串 "cat" 和 "hat"，所以答案是 3 + 3 = 6。

思路：
    1. 哈希表统计计数
    2. 公共子序列问题（words中的每一个word是否是chars的子序列）
       不行：公共子序列要求字母出现的顺序相同，该提示可以顺序不同的
'''

from collections import Counter


class Solution:
    ''' hash表统计计数 '''

    def countCharacters(self, words, chars):
        if not chars or not words:
            return 0

        sumLength = 0

        # 统计 chars 字母：出现次数 hash table
        hash_chars = Counter(chars)
        # print(hash_chars, type(hash_chars), hash_chars.keys())

        # 遍历 words, 统计每一个单词与chars的拼写情况
        i = 0
        for word in words:
            hash_word = Counter(word)
            # print(hash_word)
            'TODO: 对比hash_word和hash_chars，是否满足拼写条件，返回对应长度 or 0'
            sumLength += self.compareSpell(hash_word, hash_chars)
            i += 1
            if i == 4:
                break
        return sumLength

    def compareSpell(self, hash_word, hash_chars):
        length = 0
        for k, v in hash_word.items():
            # print(k, '--->', v, hash_chars[k])
            if k not in hash_chars.keys():
                return 0
            else:
                if hash_word[k] <= hash_chars[k]:
                    length += hash_word[k]
                else:
                    return 0
        return length


if __name__ == '__main__':
    # words = ["cat","bt","hat","tree"]
    # chars = "atach"
    # words = ["hello","world","leetcode"]
    # chars = "welldonehoneyr"
    words = ["dyiclysmffuhibgfvapygkorkqllqlvokosagyelotobicwcmebnpznjbirzrzsrtzjxhsfpiwyfhzyonmuabtlwin",
             "ndqeyhhcquplmznwslewjzuyfgklssvkqxmqjpwhrshycmvrb",
             "ulrrbpspyudncdlbkxkrqpivfftrggemkpyjl", "boygirdlggnh",
             "xmqohbyqwagkjzpyawsydmdaattthmuvjbzwpyopyafphx",
             "nulvimegcsiwvhwuiyednoxpugfeimnnyeoczuzxgxbqjvegcxeqnjbwnbvowastqhojepisusvsidhqmszbrnynkyop",
             "hiefuovybkpgzygprmndrkyspoiyapdwkxebgsmodhzpx", "juldqdzeskpffaoqcyyxiqqowsalqumddcufhouhrskozhlmobiwzxnhdkidr",
             "lnnvsdcrvzfmrvurucrzlfyigcycffpiuoo", "oxgaskztzroxuntiwlfyufddl",
             "tfspedteabxatkaypitjfkhkkigdwdkctqbczcugripkgcyfezpuklfqfcsccboarbfbjfrkxp",
             "qnagrpfzlyrouolqquytwnwnsqnmuzphne", "eeilfdaookieawrrbvtnqfzcricvhpiv", "sisvsjzyrbdsjcwwygdnxcjhzhsxhpceqz",
             "yhouqhjevqxtecomahbwoptzlkyvjexhzcbccusbjjdgcfzlkoqwiwue",
             "hwxxighzvceaplsycajkhynkhzkwkouszwaiuzqcleyflqrxgjsvlegvupzqijbornbfwpefhxekgpuvgiyeudhncv",
             "cpwcjwgbcquirnsazumgjjcltitmeyfaudbnbqhflvecjsupjmgwfbjo", "teyygdmmyadppuopvqdodaczob",
             "qaeowuwqsqffvibrtxnjnzvzuuonrkwpysyxvkijemmpdmtnqxwekbpfzs", "qqxpxpmemkldghbmbyxpkwgkaykaerhmwwjonrhcsubchs"]

    chars = "usdruypficfbpfbivlrhutcgvyjenlxzeovdyjtgvvfdjzcmikjraspdfp"
    res = Solution().countCharacters(words, chars)
    print(res)

    # a = Counter("boygirdlggnh")
    # b = Counter(chars)
    # # a = Counter("cat")
    # # b = Counter("atach")
    # print(sorted(a.items(), key=lambda x:x[1], reverse=True))
    # print(sorted(b.items(), key=lambda x:x[1], reverse=True))
    # print(Solution().compareSpell(a, b))
