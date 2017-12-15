#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: HansHuang
# Created Time : 2017年12月14日 星期四 21时36分23秒
# File Name: daily.py
# Description:
"""
import logging
from time import sleep

"""
一个青蛙一次可以跳上1级台阶,也可以跳上2级,求该青蛙跳上一个n级阶梯共有多少种跳法
4 杨氏矩阵查找
在一个m行n列二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。


def ysjz(alist,aim):
    n,m = 0,len(alist[0])-1
    while n < len(alist) and m >= 0:
        if alist[n][m] == aim:
            return True
        elif alist[n][m] > aim:
            m = m - 1
        else:
            n = n + 1
    print('n:{0},m:{1}'.format(n,m))
    return False

if __name__ == '__main__':
    alist = [
            [1,2,3,4],
            [6,7,8,9],
            [11,12,13,14],
            [16,17,18,19],
            [21,22,23,24]
            ]
    print(ysjz(alist,6))



链表成对转换
"""
class ListNode:
    def __init__(self,val):
        self.val = val
        self.next = None
"""
def reverseListNode(head):
    res = ListNode(0)
    res.next = head
    local = res
    while head.next:
        temp = head.next.next
        head.next.next = head
        local.next = head.next
        head.next = temp
        local = head
        if local.next:
            head = local.next
        else:
            break
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
    res = reverseListNode(a)
    while res:
        print(res.val)
        res = res.next

合并两个有序列表
def merge(list1,list2):
    i,j = 0,0
    res = []
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            res.append(list1[i])
            i = i + 1
        else:
            res.append(list2[j])
            j = j + 1
    if i < len(list1):
        res = res + list1[i:]
    if j < len(list2):
        res = res + list2[j:]
    return res

if __name__ == '__main__':
    a = [1,3,5,7,8,9]
    b = [2,4,5,6,7,8,10,11,12,13]
    print(merge(a,b))


def getsame(a,b):
    alength = 0
    blength = 0
    tempa,tempb = a,b
    while tempa.next:
        alength = alength + 1
        tempa=tempa.next
    while tempb.next:
        blength = blength + 1
        tempb=tempb.next
    if tempa is not tempb:
        return False
    if alength > blength:
        for i in range(alength-blength):
            a = a.next
    else:
        for i in range(blength-alength):
            b = b.next
    while a and b:
        if a.next == b.next:
            return a.next
        else:
            a = a.next
            b = b.next

   
if __name__ == '__main__':
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)
    d = ListNode(4)
    e = ListNode(5)
    f = ListNode(6)
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    f.next = c
    res = node(a,f)
    print(res) 
"""

"""
二分查找
def binarysearch(alist,aim):
    left,right = 0,len(alist)-1
    while left <= right:
        mid = (left+right) // 2
        if alist[mid] == aim:
            return mid
        elif alist[mid] < aim:
            left = mid + 1
        else:
            right = mid - 1
    return None

快排
"""
#冒泡
def BubbleSort(alist):
    for index in range(len(alist)-1,0,-1):
        for local in range(index):
            if alist[local] > alist[local+1]:
                alist[local],alist[local+1] = alist[local+1],alist[local]
    return alist

#冒泡找第rank大的数
def fingsecond(alist,rank):
    if rank < 1 or rank > len(alist) - 1:
        return None
    for index in range(len(alist)-1,len(alist)-1-rank,-1):
        for local in range(index):
            if alist[local] > alist[local+1]:
                alist[local],alist[local+1] = alist[local+1],alist[local]
    return alist[local+1]

#选择排序
def chooseSort(alist):
    for index in range(len(alist)-1,0,-1):
        temp = 0
        for local in range(index+1):
            if alist[local] > alist[temp]:
                temp = local
        alist[temp],alist[index] = alist[index],alist[temp]
    return alist

#插入排序
def insertSort(alist):
    for index in range(1,len(alist)):
        curval = alist[index]
        while alist[index-1] > curval and index > 0:
            alist[index] = alist[index-1]
            index = index - 1
        alist[index] = curval
    return alist

#归并排序
def mergeSort(alist):
    if len(alist) < 2:
        return alist
    mid = len(alist) // 2
    lefthalf = mergeSort(alist[:mid])
    righthalf = mergeSort(alist[mid:])
    i,j,m = 0,0,0
    res = [None] * (len(alist))
    while i < len(lefthalf) and j < len(righthalf):
        if lefthalf[i] < righthalf[j]:
            res[m] = lefthalf[i]
            i = i + 1
            m = m + 1
        else:
            res[m] = righthalf[j]
            j = j + 1
            m = m + 1
    while i < len(lefthalf):
        res[m] = lefthalf[i]
        m = m + 1
        i = i + 1
    while j < len(righthalf):
        res[m] = righthalf[j]
        m =m + 1
        j = j + 1

    return res

#快速排序
def quickSort(alist):
    quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
    if first < last:
        splitpoint = partition(alist,first,last)
        quickSortHelper(alist,first,splitpoint-1)
        quickSortHelper(alist,splitpoint+1,last)

def partition(alist,first,last):
    left = first + 1
    right = last
    curval = alist[first]
    done = False
    while not done:
        while left <= right and alist[left] <= curval:
            left = left + 1
        while left <= right and alist[right] >= curval:
            right = right - 1
        if left > right:
            done = True
        else:
            alist[left],alist[right] = alist[right],alist[left]
    alist[first],alist[right] = alist[right],alist[first]
    return right


def part(alist,first,last):
    left = first + 1
    right = last
    done = False
    curval = alist[first]
    while not done:
        while left <= right and alist[left] <= curval:
            left = left + 1
        while left <= right and alist[right] >= curval:
            right = right - 1
        if left  > right:
            done = True
        else:
            alist[left],alist[right] = alist[right],alist[left]
    alist[first],alist[right] = alist[right],alist[first]
    return right

def partHelper(alist,first,last):
    if first < last:
        splitpoint = part(alist,first,last)
        partHelper(alist,first,splitpoint-1)
        partHelper(alist,splitpoint+1,last)

def main(alist):
    partHelper(alist,0,len(alist)-1)


if __name__ == '__main__':
    a = [1,1,121321,212,321,543,7,32,6757,4323,7,7,12,22,65,8,3,5]
    main(a)
    print(a)













