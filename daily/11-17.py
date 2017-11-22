#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: HansHuang
# Created Time : 2017年11月17日 星期五 10时29分26秒
# File Name: daily.py
# Description:
"""
from collections import Counter
import logging
logging.basicConfig(level=logging.INFO,format='%(asctime)s %(filename)s : %(levelname)s %(message)s',datefmt='%Y-%m-%d %A %H:%M:%S')
"""
Given an array of strings, group anagrams together.
For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"],
Return:
[
  ["ate", "eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note: All inputs will be in lower-case.

class Solution():
    def anagrams(self,strs):
        res = []
        for i in strs:
            for s in range(len(res)):
                if Counter(i) == Counter(res[s][0]):
                    res[s].append(i)
                    break
            else:
                res.append([i,])
        return res

if __name__ == '__main__':
    s = Solution()
    a = ['eat','ate','tan','ant','abc']
    logging.info(s.anagrams(a))
"""
"""
Problem Statement
Given two strings, find the longest common substring.
Return the length of it.
Notice
The characters in substring should occur continuously in original string. This is different with subsequence.
Example
Given A = "ABCD", B = "CBCE", return 2.
Challenge **
O(n x m) time and memory.

class Solution:
 

    #因为下面的字符串例子里也有另外一个a,我在外层循环重置temp,内层循环没有重置,所以又判断相等了一次,so多了一次
    def longestCommonSubstring(self, A, B):
        if not (A and B):
            return 0
        res = 0
        for i in range(len(A)):
            temp = 0
            logging.info('初始化temp{0}'.format(temp))
            for j in range(len(B)):
                while i+temp < len(A) and j+temp < len(B) and A[i+temp] == B[j+temp]:
                    temp += 1
                    logging.info('此时a的第{0}个数{1}与b的第{2}个数{3}相等'.format(i+temp,A[i+temp],j+temp,B[j+temp]))
                    logging.info('此时temp等于{0}'.format(temp))
                if temp > res:
                    logging.info('推出循环,temp大于res,此时temp={0},res={1}'.format(temp,res))
                    res = temp
        logging.info('方法一结束')
        return res

    def standard(self,A,B):
        if not (A and B):
            return 0
        lcs = 0
        for i in range(len(A)):
            for j in range(len(B)):
                lcs_temp = 0
                while (i+lcs_temp<len(A) and j+lcs_temp<len(B) and A[lcs_temp+i] == B[lcs_temp+j]):
                    lcs_temp += 1
                if lcs_temp > lcs:
                    lcs = lcs_temp
        return lcs


if __name__ == '__main__':
    s = Solution()
    a = 'abcdefg'
    b = 'abcfsadas'
    logging.info(s.longestCommonSubstring(a,b))
    logging.info(s.standard(a,b))
"""
"""
旋转字符串
给定一个字符串和一个偏移量，根据偏移量旋转字符串(从左向右旋转)
样例
对于字符串 "abcdefg".
offset=0 => "abcdefg"
offset=1 => "gabcdef"
offset=2 => "fgabcde"
offset=3 => "efgabcd"
"""
class Solution:
    """
    @param: str: An array of char
    @param: offset: An integer
    @return: nothing
    """
    def rotateString(self, str, offset):
        if (str and offset) is None:
            return 0
        offset = offset % len(str)
        return str[len(str)-offset::-1]+str[:len(str)-offset]

if __name__ == '__main__':
    s = Solution()
    print(s.rotateString('abcdwfg',3))
