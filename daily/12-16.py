#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: HansHuang
# Created Time : 2017年12月16日 星期六 12时05分35秒
# File Name: daily.py
# Description:
"""
import logging
from collections import Counter
"""
单链表翻转
class ListNode:
    def __init__(self,val):
        self.val = val
        self.next = None

def reverse(head):
    res = ListNode(0)
    while head:
        temp = head.next
        head.next = res.next
        res.next = head
        head = temp
    return res.next

if __name__ == '__main__':
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)
    d = ListNode(4)
    e = ListNode(5)
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    res = reverse(a)
    while res:
        print(res.val)
        res = res.next

检查字符串是否是变位词
"""
#使用counter
def checkstr1(a,b):
    return Counter(a) == Counter(b)

#使用字典
def checkstr2(a,b):
    adict = {}
    bdict = {}
    for char in a:
        if char in adict:
            adict[char] += 1
        else:
            adict[char] = 1
    for char2 in b:
        if char2 in bdict:
            bdict[char2] += 1
        else:
            bdict[char2] = 1
    return adict == bdict
 

#排序
def checkstr3(a,b):
    return sorted(a) == sorted(b)


#约瑟夫环
def yue(alist,k):
    temp = 0
    while len(alist) > 1:
        for i in range(k):
            if temp < len(alist) - 1:
                temp = temp + 1
            else:
                temp = 0
        alist.pop(temp)
    return alist[-1]

#一个汽水一块钱,两个空瓶换一瓶
def drinks(money):
    sumdrinks = 0
    empty = 0
    availdrinks = money
    while availdrinks:
        sumdrinks += availdrinks
        empty += availdrinks
        availdrinks = 0
        if empty > 1:
            availdrinks = empty // 2
            empty = empty % 2
    return sumdrinks


#升序自然数序列,有重复数字,返回给定值的边界索引
def binaryleft(alist,key):
    left = 0
    right = len(alist) - 1
    while left <= right:
        mid = (left+right) // 2
        if alist[mid] < key:
            left = mid + 1
        else:
            right = mid - 1
    if alist[left] == key:
        return left

def binaryright(alist,key):
    left,right = 0,len(alist)-1
    while left <= right:
        mid = (left+right) // 2
        if alist[mid] <= key:
            left = mid + 1
        else:
            right = mid - 1
    if alist[right] == key:
        return right



def binaryfind(alist,key):
    return binaryleft(alist,key),binaryright(alist,key)



if __name__ == '__main__':
    alist=[1,2,3,4,6,7,7,7,8,9,10,11]
    print(binaryfind(alist,7))

