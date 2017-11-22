#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: HansHuang
# Created Time : 2017年11月16日 星期四 20时34分20秒
# File Name: daily.py
# Description:

Implement strStr().+
Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
class Solution:
    def strStr(self,source,target):
        for s in range(len(source)):
            if source[s] == target[0]:
                print('相等了{0},{1}'.format(source[s],target[0]))
                t = 0
                temp = s
                while t < len(target) and target[t] == source[s]:
                    print('相等了{0},{1}'.format(source[s],target[t]))
                    t = t + 1
                    s = s + 1
                if t == len(target):
                    return temp
                else:
                    return -1
        return -1 

    def sandard(self, source, target):
        if source is None or target is None:
            return -1
        for i in range(len(source)-len(target)+1):
            for j in range(len(target)):
                if source[i+j] != target[j]:
                    break
            else:
                print('现在执行了')
                return i
        return -1

    #KMP算法还不会

两个字符串是变位词 
写出一个函数 anagram(s, t) 判断两个字符串是否可以通过改变字母的顺序变成一样的字符串
样例
给出 s = "abcd"，t="dcab"，返回 true.
给出 s = "ab", t = "ab", 返回 true.
给出 s = "ab", t = "ac", 返回 false.


from collections import Counter
class Solution:
 
    def anagram(self, s, t):
        return Counter(s) == Counter(t)


比较字符串
比较两个字符串A和B，确定A中是否包含B中所有的字符。字符串A和B中的字符都是 大写字母
注意事项
在 A 中出现的 B 字符串里的字符不需要连续或者有序。
样例
给出 A = "ABCD" B = "ACD"，返回 true
给出 A = "ABCD" B = "AABC"， 返回 false

"""
class Solution:
    """
    @param: A: A string
    @param: B: A string
    @return: if string A contains all of the characters in B return true else return false
    """
    def compareStrings(self, A, B):
        for a in A:


if __name__ == '__main__':
    s = Solution()
    print(s.sandard('abcdefg','efg'))

