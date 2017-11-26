#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: HansHuang
# Created Time : 2017年11月26日 星期日 12时20分09秒
# File Name: daily.py
# Description:
"""
import logging
logging.basicConfig(level=logging.INFO,format='%(asctime)s %(filename)s : %(levelname)s %(message)s',datefmt='%Y-%m-%d %A %H:%M:%S')

class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

"""
链表插入排序
用插入排序对链表排序
样例
Given 1->3->2->0->null, return 0->1->2->3->null

class Solution:
    #感觉这段代码有点丑陋,与表达式如果后面的条件建立于前面条件的基础上,
    #那顺序一定不能搞反,不然会抛出NoneType的错误
    def insertionSortList(self, head):
        if head and head.next is None:
            return head
        res = head
        done = head.next
        head.next = None
        while done:
            head = res
            while head.next and  head.next.val < done.val:
                head = head.next
            temp = done.next
            done.next = head.next
            head.next = done
            head = res
            done = temp
        return res

回文链表

class Solution:
    
    #使用了辅助栈,需要额外的空间
    def isPalindrome(self,head):
        stack = []
        temp = head
        while temp:
            stack.append(temp.val)
            temp = temp.next
        while head:
            if head.val == stack.pop():
                head = head.next
            else:
                return False
        return True

    #使用递归
    def standard(self,head):
        result = [head,True]
        self.helper(head,result)
        return result[1]

    def helper(self,right,result):
        if right:
            self.helper(right.next,result)
            is_pal = result[0].val == right.val and result[1]
            result = [result[0].next,is_pal]


旋转链表
给定一个链表，旋转链表，使得每个节点向右移动k个位置，其中k是一个非负数
样例
给出链表1->2->3->4->5->null和k=2
返回4->5->1->2->3->null

class Solution:
    #教科书般的代码,感觉没有缺点,时间复杂度啊O(2n),还阔以 
    def rotateRight(self, head, k):
        if k == 0:
            return head
        fast = head
        while k > 0:
            if fast.next:
                fast = fast.next
            else:
                fast = head
            k -= 1
        slow = head
        while fast.next:
            slow = slow.next
            fast = fast.next
        temp = slow.next
        slow.next = None
        fast.next = head
        return temp

两两交换链表中的节点
给一个链表，两两交换其中的节点，然后返回交换后的链表。
样例
给出 1->2->3->4, 你应该返回的链表是 2->1->4->3。



class Solution:
    #这段代码言简意赅,没毛病
    #思路就是两两调换嘛,需要一个额外节点空间保存头节点,不然head遍历到后面无法返回
    def swapPairs(self, head):
        if not head.next:
            return head
        node = ListNode(0)
        res = node
        node.next = head
        while node.next and node.next.next:
            temp = node.next.next
            node.next.next = temp.next
            temp.next = node.next
            node.next = temp
            node = temp.next
        return res.next


删除链表中的元素
删除链表中等于给定值val的所有节点。
样例
给出链表 1->2->3->3->4->5->3, 和 val = 3, 你需要返回删除3之后的链表：1->2->4->5。
"""

class Solution:
    #开心!
    def removeElements(self, head, val):
        if not head:
            return head
        res = ListNode(0)
        res.next = head
        temp = res
        while temp and temp.next:
            if temp.next.val == val:
                temp.next = temp.next.next
                temp = temp.next
            else:    
                temp = temp.next
        return res.next

if __name__ == '__main__':
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)
    d = ListNode(4)
    e = ListNode(5)
    f = ListNode(6)
    g = ListNode(7)
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = f
    f.next = g
    s = Solution()
    res = s.removeElements(a,7)
    while res:
        print(res.val)
        res = res.next

