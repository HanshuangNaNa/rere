#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: HansHuang
# Created Time : 2017年11月24日 星期五 11时06分31秒
# File Name: daily.py
# Description:
"""
import logging
import sys
logging.basicConfig(level=logging.INFO,format='%(asctime)s %(filename)s : %(levelname)s %(message)s',datefmt='%Y-%m-%d %A %H:%M:%S')
sys.setrecursionlimit(10000)


class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
翻转链表2
翻转链表中第m个节点到第n个节点的部分
注意事项
m，n满足1 ≤ m ≤ n ≤ 链表长度
样例
给出链表1->2->3->4->5->null， m = 2 和n = 4，返回1->4->3->2->5->null


class Solution:
  
    #还阔以,时间复杂度啊在O(n)
    def reverseBetween(self, head, m, n):
        res = head
        count = n - m
        while m > 1:
            splitnode = head
            head = head.next
            m -= 1
        logging.info('分割点找出,split:{0},head:{1}'.format(splitnode.val,head.val))
        while count > 0:
            temp = head.next
            head.next = head.next.next
            temp.next = splitnode.next
            splitnode.next = temp
            count -= 1
            logging.info('还剩{0}次交换,此时split下一个是{1},head位于{2}'.format(count,splitnode.next.val,head.val))
        return res


合并两个排序链表 
将两个排序链表合并为一个新的排序链表
样例
给出 1->3->8->11->15->null，2->null， 返回 1->2->3->8->11->15->null。



class Solution:

    def mergeTwoLists(self, l1, l2):
        head = ListNode(0)
        res = head
        while l1 and l2:
            if l1.val < l2.val:
                temp = l1.next
                l1.next = None
                head.next = l1
                head = head.next
                l1 = temp
            else:
                temp = l2.next
                l2.next = None
                head.next = l2
                head = head.next
                l2 = temp
        if l1 is not None:
            head.next = l1
        elif l2 is not None:
            head.next = l2
        return res.next

合并k个排序链表
合并k个排序链表，并且返回合并后的排序链表。尝试分析和描述其复杂度。
样例
给出3个排序链表[2->4->null,null,-1->null]，返回 -1->2->4->null


class Solution:
   
    def mergeKLists(self, lists):
        while len(lists) > 1:
            head = ListNode(0)
            res = head
            l1 = lists.pop()
            l2 = lists.pop()
            while l1 and l2:
                if l1.val < l2.val:
                    temp = l1.next
                    l1.next = None
                    head.next = l1
                    head = head.next
                    l1 = temp
                else:
                    temp = l2.next
                    l2.next = None
                    head.next = l2
                    head = head.next
                    l2 = temp
            if l1 is not None:
                head.next = l1
            elif l2 is not None:
                head.next = l2
            lists.append(res.next)
        return lists[-1]

重排链表 
给定一个单链表L: L0→L1→…→Ln-1→Ln,
重新排列后为：L0→Ln→L1→Ln-1→L2→Ln-2→…
必须在不改变节点值的情况下进行原地操作。
样例
给出链表 1->2->3->4->null，重新排列后为1->4->2->3->null。


class Solution:

    def reorderList(self, head):
        if not head or not head.next:
            return head
链表排序
在 O(n log n) 时间复杂度和常数级的空间复杂度下给链表排序。
样例
给出 1->3->2->null，给它排序变成 1->2->3->null.

"""
def sortList(head):
    left = head
    right = support(head)
    if left.next and right.next:
        left = sortList(left)
        right = sortList(right)
    res = ListNode(0)
    head = res
    while left and right:
        if left.val < right.val:
            temp = left.next
            left.next = None
            head.next = left
            head = head.next
            left = temp
        else:
            temp = right.next
            right.next = None
            head.next = right
            head = head.next
            right = temp
    if left:
        head.next = left
    if right:
        head.next = right
    return res.next

#做个辅助函数找到归并排序的中心点
def support(head):
    if head.next and not head.next.next:
        return head.next
    elif head.next is None:
        return head
    slow,fast = head,head.next
    while fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow




if __name__ == '__main__':
    a = ListNode(5)
    b = ListNode(9)
    c = ListNode(20)
    d = ListNode(54)
    e = ListNode(12)
    f = ListNode(88)
    g = ListNode(4)
    h = ListNode(36)
    j = ListNode(1)
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = f
    g.next = h
    h.next = j
    red = sortList(a)
    while red:
        print(red.val)
        red = red.next
