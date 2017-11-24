#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: HansHuang
# Created Time : 2017年11月23日 星期四 11时26分37秒
# File Name: daily.py
# Description:
"""
import logging
logging.basicConfig(level=logging.INFO,format='%(asctime)s %(filename)s : %(levelname)s %(message)s',datefmt='%Y-%m-%d %A %H:%M:%S')
"""
Remove Duplicates from Sorted List
给定一个排序链表，删除所有重复的元素每个元素只留下一个。
样例
给出 1->1->2->null，返回 1->2->null
给出 1->1->2->3->3->null，返回 1->2->3->null
"""

class ListNode(object):
    def __init__(self, val,next=None):
        self.val = val
        self.next = next

"""
class Solution: 
    def deleteDuplicates(self, head):
        res = ListNode(0)
        res.next = head
        while head.next:
            if head.val == head.next.val:
                head.next = head.next.next
            else:
                head = head.next
        return res

删除排序链表中的重复数字 II
给定一个排序链表，删除所有重复的元素只留下原链表中没有重复的元素。
样例
给出 1->2->3->3->4->4->5->null，返回 1->2->5->null
给出 1->1->1->2->3->null，返回 2->3->null

class Solution:
    #边界值检查有点问题
    def deleteDuplicates(self, head):
        res = ListNode(0)
        res.next = head
        temp = res
        while head.next:
            if head.val == head.next.val:
                while head.next and head.val == head.next.val:
                    head = head.next
                    logging.info(head)
                temp.next = head.next
                if head.next:
                    head = head.next
            else:
                temp = head
                head = head.next
        return res

    def review(self,head):
        res = ListNode(0)
        res.next = head
        temp = res
        while temp.next and temp.next.next:
            if temp.next.val == temp.next.next.val:
                val_temp = temp.next.val
                while temp.next and temp.next.val == val_temp:
                    temp.next = temp.next.next
            else:
                temp = temp.next
        return res.next

    def standard(self,head):
        if head is None:
            return None
        dummy = ListNode(0)
        dummy.next = head
        node = dummy
        while node.next is not None and node.next.next is not None:
            if node.next.val == node.next.next.val:
                val_prev = node.next.val
                while node.next is not None and node.next.val == val_prev:
                    node.next = node.next.next
            else:
                node = node.next

链表划分 
给定一个单链表和数值x，划分链表使得所有小于x的节点排在大于等于x的节点之前。
你应该保留两部分内链表节点原有的相对顺序。
样例
给定链表 1->4->3->2->5->2->null，并且 x=3
返回 1->2->2->4->3->5->null


class Solution:
   
    def partition(self, head, x):
        start = ListNode(0)
        res = start
        end = ListNode(x)
        start.next = end
        while head:
            if head.val < x:
                temp = head.next
                head.next = start.next
                start.next = head
                start = start.next
                head = temp
            else:
                temp = head.next
                end.next = head
                end.next.next = None
                end = end.next
                head = temp
        start.next = start.next.next 
        return res.next

链表求和 
你有两个用链表代表的整数，其中每个节点包含一个数字。数字存储按照在原来整数中相反的顺序，使得第一个数字位于链表的开头。写出一个函数将两个整数相加，用链表形式返回和。
样例
给出两个链表 3->1->5->null 和 5->9->2->null，返回 8->0->8->null


class Solution:
 
    def addLists(self, l1, l2):
        res = ListNode(0)
        index = res
        temp = 0 
        while l1 and l2:
            index.next = ListNode(temp+(l1.val+l2.val)%10)
            temp = (l1.val+l2.val) // 10
            index = index.next
            l1 = l1.next
            l2 = l2.next
        if l1:
            index.next = l1
        if l2:
            index.next = l2
        return res.next

翻转链表
翻转一个链表
样例
给出一个链表1->2->3->null，这个翻转后的链表为3->2->1->null

class Solution:
 
    def reverse(self, head):
        res = ListNode(0)
        index = res
        while head:
            temp = head.next
            head.next = res.next
            res.next = head
            head = temp
        return res.next

删除链表中倒数第n个节点
给定一个链表，删除链表中倒数第n个节点，返回链表的头节点。
注意事项
链表中的节点个数大于等于n
样例
给出链表1->2->3->4->5->null和 n = 2.
删除倒数第二个节点之后，这个链表将变成1->2->3->5->null.



class Solution:

    def removeNthFromEnd(self, head, n):
        count = 0
        temp = head
        slow = temp
        while head.next:
            if count < n:
                count += 1
                head = head.next
            else:
                slow = slow.next
                head = head.next
        slow.next = slow.next.next
        return temp

带环链表
给定一个链表，判断它是否有环。
样例
给出 -21->10->4->5, tail connects to node index 1，返回 true
"""
class Solution:

    def hasCycle(self, head):
        
        slow = head
        fast = head.next
        while fast.next and slow.next.next:
            if fast == slow:
                return True
            else:
                fast = fast.next.next
                slow = slow.next
        return False





if __name__ == '__main__':
    a = ListNode(1)
    b = ListNode(4)
    c = ListNode(3)
    d = ListNode(2)
    e = ListNode(5)
    f = ListNode(2)
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = f 
    f.next = a
    s = Solution()
    print(s.hasCycle(a))

    """
    while res:
        print(res.val)
        res = res.next
    """
