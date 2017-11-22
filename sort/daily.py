#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: HansHuang
# Created Time : 2017年11月15日 星期三 10时42分56秒
# File Name: daily.py
# Description:
整数排序
给一组整数，按照升序排序，使用选择排序，冒泡排序，插入排序或者任何 O(n2) 的排序算法。
样例
对于数组 [3, 2, 1, 4, 5], 排序后为：[1, 2, 3, 4, 5]。

class Solution:
  
    def sortIntegers(self, A):
        # write your code here
        for index in range(1,len(A)):
            value = A[index]
            while index > 0 and A[index-1] > value:
                A[index] = A[index-1]
                index = index - 1
            A[index] = value
        return A 

链表插入排序
用插入排序对链表排序
样例
Given 1->3->2->0->null, return 0->1->2->3->null
"""
"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next



class Solution:
    def insertionSortList(self, head):
        # write your code here
        dummy = ListNode(0)
        while head:
            temp = dummy
            headnext = head.next
            while temp.next and temp.next < head.val:
                temp = temp.next
            head.next = temp.next
            temp.next = head
            head = headnext
        return dummy.next


两数组的交
样例
nums1 = [1, 2, 2, 1], nums2 = [2, 2], 返回 [2].

class Solution:
    def simple(self,nums1,nums2):
        return list(set(nums1) & set(nums2)) 


    def intersection(self, nums1, nums2):
        res = []
        for n1 in nums1:
            for n2 in nums2:
                if n1 == n2 and n1 not in res:
                    res.append(n1)
        return res

整数排序 II
给一组整数，按照升序排序。使用归并排序，快速排序，堆排序或者任何其他 O(n log n) 的排序算法。
样例
给出 [3, 2, 1, 4, 5], 排序后的结果为 [1, 2, 3, 4, 5]。

#写一个快排,还没写完
def sortIntegers2(alist):
    quicksorthelp(alist,1,len(alist)-1)

def quicksorthelp(alist,left,right):
    if left<right:
        point = quicksort(alist,left,right)
        quicksorthelp(alist,left,point-1)
        quicksorthelp(alist,point+1,right)


def quicksort(alist,left,right):
    mid = alist[left-1]
    done = False
    while not done:
        while alist[left] < alist[mid] and left <= right:
            left = left + 1
        while alist[right] > alist[mid] and left <= right:
            right = right + 1
        if right < left:
            done = True
        else:
            alist[left],alist[right] = alist[right],alist[left]
    alist[right],alist[mid] = alist[mid],alist[right]
    return right


合并区间
给出若干闭合区间，合并所有重叠的部分。
样例
给出的区间列表 => 合并后的区间列表：
[                     [
  [1, 3],               [1, 6],
  [2, 6],      =>       [8, 10],
  [8, 10],              [15, 18]
  [15, 18]            ]
]
"""
class Solution:
 
    def merge(self, intervals):
        for i in range(len(intervals)):



if __name__ == '__main__':


