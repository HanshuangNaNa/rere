#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: HansHuang
# Created Time : 2017年11月19日 星期日 13时35分03秒
# File Name: daily.py
# Description:
"""
import logging
logging.basicConfig(level=logging.INFO,format='%(asctime)s %(filename)s : %(levelname)s %(message)s',datefmt='%Y-%m-%d %A %H:%M:%S')

"""
翻转字符串
给定一个字符串，逐个翻转字符串中的每个单词。
说明
单词的构成：无空格字母构成一个单词
输入字符串是否包括前导或者尾随空格？可以包括，但是反转后的字符不能包括
如何处理两个单词间的多个空格？在反转字符串中间空格减少到只含一个
class Solution:

    def reverseWords(self, s):
        return ''.join(reversed(s.strip().split()))

有效回文串
给定一个字符串，判断其是否为一个回文串。只包含字母和数字，忽略大小写。
注意事项
你是否考虑过，字符串有可能是空字符串？这是面试过程中，面试官常常会问的问题。
在这个题目中，我们将空字符串判定为有效回文。
样例
"A man, a plan, a canal: Panama" 是一个回文。
"race a car" 不是一个回文。



class Solution:

    def isPalindrome(self, s):
        s = s.upper()
        left = 0
        right = len(s) - 1
        flag = True
        while left < right:
            if s[left] == ' ':
                left = left + 1
            elif s[right] == ' ':
                right = right - 1
            elif s[left] != s[right]:
                return False
            left = left + 1
            right = right - 1
        return True

最长回文子串
给出一个字符串（假设长度最长为1000），求出它的最长回文子串，你可以假定只有一个满足条件的最长回文串。
样例
给出字符串 "abcdzdcab"，它的最长回文子串为 "cdzdc"。


class Solution:
    #我这个比较吊,独创流派
    def longestPalindrome(self, s):
        res = ''
        count = 0
        for index in range(1,len(s)-1):
            temp = 1
            if s[index-temp] == s[index+temp]:
                while s[index-temp] == s[index+temp] and index-temp>0 and index+temp<len(s):
                    temp += 1
                counttemp = temp*2-1
                if counttemp > count:
                    res = s[index-temp-1:index+temp+2]
            elif s[index] == s[index+1]:
                logging.info('此时两个数{0},{1}相等'.format(s[index],s[index+1]))
                left,right = index,index+1
                while s[left] == s[right] and left > 0 and right < len(s) - 1:
                    logging.info('进入循环')
                    left -= 1
                    right += 1
                    logging.info('left={0},right={1}'.format(left,right))
                if right -left > count:
                    logging.info('此时{0}-{1}>{2}'.format(right,left,count))
                    res = s[left+1:right]
        return res 

    #穷竭搜索
    def standard(self,s):
        if not s:
            return ""
        n=len(s)
        longest,left,right=0,0,0
        for i in xrange(0,n):
            for j in xrange(i+1,n+1):
                substr = s[i:j]
                if self.isPalindrome(substr) and len(substr) > longest:
                    longest = len(substr)
                    left,right = i,j
        result = s[left:right]
        return result

    def isPalindrome(self,s):
        if not s:
            return False
        return s == s[::-1]

空格替换
设计一种方法，将一个字符串中的所有空格替换成 %20 。你可以假设该字符串有足够的空间来加入新的字符，且你得到的是“真实的”字符长度。
你的程序还需要返回被替换后的字符串的长度。
注意事项
如果使用 Java 或 Python, 程序中请用字符数组表示字符串。
样例
对于字符串"Mr John Smith", 长度为 13
替换空格之后，参数中的字符串需要变为"Mr%20John%20Smith"，并且把新长度 17 作为结果返回。

class Solution:

    def replaceBlank(self, string, length):
        res = '%20'.join(string.split())
        logging.info(res)
        return len(res)

通配符匹配
判断两个可能包含通配符“？”和“*”的字符串是否匹配。匹配规则如下：
'?' 可以匹配任何单个字符。
'*' 可以匹配任意字符串（包括空字符串）。
两个串完全匹配才算匹配成功。
函数接口如下:
bool isMatch(const char *s, const char *p)
样例
一些例子：
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "*") → true
isMatch("aa", "a*") → true
isMatch("ab", "?*") → true
isMatch("aab", "c*a*b") → false


最后一个单词的长度
给定一个字符串， 包含大小写字母、空格' '，请返回其最后一个单词的长度。
如果不存在最后一个单词，请返回 0 。
注意事项
一个单词的界定是，由字母组成，但不包含任何的空格。
样例
给定 s = "Hello World"，返回 5。

class Solution:
    
    def lengthOfLastWord(self, s):
        alist = s.split()
        return len(alist[-1])


报数
报数指的是，按照其中的整数的顺序进行报数，然后得到下一个数。如下所示：
1, 11, 21, 1211, 111221, ...
1 读作 "one 1" -> 11.
11 读作 "two 1s" -> 21.
21 读作 "one 2, then one 1" -> 1211.
给定一个整数 n, 返回 第 n 个顺序。
注意事项
整数的顺序将表示为一个字符串。
样例
给定 n = 5, 返回 "111221".
"""

class Solution:

    def countAndSay(self, n):
        
"""
if __name__ == '__main__':
    s = Solution()
    print(s.replaceBlank('ap cdei ffedi cba',17))
