#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: HansHuang
# Created Time : 2017年11月06日 星期一 18时44分03秒
# File Name: daily.py
# Description:

链表求和
你有两个用链表代表的整数，其中每个节点包含一个数字。数字存储按照在原来整数中相反的顺序，使得第一个数字位于链表的开头。写出一个函数将两个整数相加，用链表形式返回和。
样例
给出两个链表 3->1->5->null 和 5->9->2->null，返回 8->0->8->null

Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None



class Solution:
 
    def addLists(self, l1, l2):
        # write your code here
        res = ListNode(0)
        head = res
        while l1.next or l2.next:
            temp = 0
            if l1.val + l2.val >= 10:
                res.val = (l1.val + l2.val) % 10 + res.val
                temp = 1
            else:
                res.val = l1.val + l2.val + res.val
            l1,l2 = l1.next,l2.next
            res.next = ListNode(temp)
            res = res.next
        return head

    def standdard(self,l1,l2):
        head = ListNode(0)
        ptr = head
        carry = 0
        while True:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            ptr.val = carry % 10
            carry = carry // 10
            if l1 or l2 or carry:
                ptr.next = ListNode(0)
                ptr = prt.next
            else:
                break
        return head

翻转链表
样例
给出一个链表1->2->3->null，这个翻转后的链表为3->2->1->null

Definition of ListNode

class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next



class Solution:

    param: head: n
    return: The new head of reversed linked list.

    def standard(self,head):
        curt = None
        while head != None:
            temp = head.next
            head.next = curt
            curt = head
            head = temp
        return curt

合并两个排序链表
将两个排序链表合并为一个新的排序链表
样例
给出 1->3->8->11->15->null，2->null， 返回 1->2->3->8->11->15->null。

"""
"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next



class Solution:

    def mergeTwoLists(self, l1, l2):
        # write your code here
        temp = ListNode(0)
        res = temp
        while l1 or l2:
            if l1.val < l2.val:
                temp.val = l1.val
                temp.next = ListNode(0)
                temp = temp.next
                l1 = l1.next
            else:
                temp.val = l2.val
                temp.next = ListNode(0)
                temp = temp.next
                l2 = l2.next
        return res

#标准答案的写法才是对的，我没有考虑到两个链表的数值差距相对较大的时候，
#其中一条链表会被全部加入到新链表中，另外一条则有剩余,标准答案才是对的

    def standard(self,l1,l2):
        dummy = ListNode(0)
        tmp = dummy
        while l1 != None and l2 != None:
            if l1.val < l2.val:
                tmp.next = l1
                l1 = l1.next
            else:
                tmp.next = l2
                l2 = l2.next
            tmp = tmp.next
        if l1 != None:
            tmp.next = l1
        else:
            tmp.next = l2
        return dummy.next


删除链表中倒数第n个节点
给定一个链表，删除链表中倒数第n个节点，返回链表的头节点。
注意事项
链表中的节点个数大于等于n
样例
给出链表1->2->3->4->5->null和 n = 2.
删除倒数第二个节点之后，这个链表将变成1->2->3->5->null.


class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
 
    def removeNthFromEndummy = ListNode(0)
        while head:
            temp = dummy
            next = head.next
            while d(self, head, n):
        # write your code here
        res = ListNode(0)
        res.next = head
        tmp = res
        for i in range(0,n):
            head = head.next
        print('此时head位于第'+str(head.val))
        print('此时tmp位于第'+str(tmp.val))
        while head != None:
            head = head.next
            tmp = tmp.next
            #print('此时head位于第'+str(head.val))
            print('此时tmp位于第'+str(tmp.val))
        print('现在我要将第n位删去'+str(tmp.next.val)+str(tmp.next.next.val))
        tmp.next = tmp.next.next
        return res.next

用插入排序对链表排序
样例
Given 1->3->2->0->null, return 0->1->2->3->null

Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next


#插入排序写一个
def insertsort(alist):
    for index in range(1,len(alist)):
        currentvalue = alist[index]
        position = index
        while position > 0 and alist[position-1]>currentvalue:
            alist[position] = alist[position-1]
            position = position - 1
        alist[position] = currentvalue



class Solution:

    def insertionSortList(self, head):
        # write your code here
        dummy = ListNode(0)
        while head:
            next = head.next
            temp = dummy
            while temp.next and temp.next.val < head.val:
                temp = temp.next
            head.next = temp.next
            temp.next = head
            head = next
        return dummy.next

删除排序链表中的重复元素
给定一个排序链表，删除所有重复的元素每个元素只留下一个。
样例
给出 1->1->2->null，返回 1->2->null
给出 1->1->2->3->3->null，返回 1->2->3->null



class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
       def deleteDuplicates(self, head):
        # write your code here
        temp = head
        point = None
        while temp:
            if temp.next and temp.val == temp.next.val:
                point = temp
                temp = temp.next
            while temp and temp.val == point.val:
                temp = temp.next
            point.next = temp
        return head

    def standard(self,head):
        delflag = 1
        flag = 1
        p = head
        while(p != None and p.next != None):
            if p.val != p.next.val:
                print('done 1:')
                flag = 1
                p = p.next
            #elif flag < delflag:
              #  print('done 2')
               # flag += 1
                #p = p.next
            else:
                print('done 3')
                p.next = p.next.next
        return head

#给定一个节点，删除链表中这个节点的，O(1)时间复杂度
    def deleteNode(self,Node):
        if Node and Node.next:
            return
        next = Node.next
        Node.val = next.val
        Node.next = next.next
        return

两两交换链表中的节点
给一个链表，两两交换其中的节点，然后返回交换后的链表。
样例
给出 1->2->3->4, 你应该返回的链表是 2->1->4->3。
Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None



class Solution:
    def swapPairs(self, head):
        # write your code here
        print('done swap')
        res = ListNode(0)
        res.next = head
        while head and head.next:
            temp = head.next.next
            head.next.next = head
            head.next = temp
            head = temp
        return res.next

    def standard(self,head):
        if head == None or head.next == None:
            return head
        dummy = ListNode(0)
        dummy.next = head
        p = dummy
        while p.next and p.next.next:
            tmp = p.next.next
            p.next.next = tmp.next
            tmp.next = p.next
            p.next = tmp
            p = p.next.next
        return dummy.next

链表划分
给定一个单链表和数值x，划分链表使得所有小于x的节点排在大于等于x的节点之前。
你应该保留两部分内链表节点原有的相对顺序。
样例
给定链表 1->4->3->2->5->2->null，并且 x=3
返回 1->2->2->4->3->5->null

class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
      def partition(self, head, x):
        # write your code here
        res = ListNode(0)
        node = ListNode(x)
        res.next = node
        front = res
        hear = node
        while head:
            if head.val < x:
                temp = head.next
                front.next = head
                head.next = node
                front = head
                head = temp
            else:
                temp = head.next
                hear.next = head
                head.next = None
                hear = head
                head = temp
        front.next = node.next
        return res.next

带环链表
给定一个链表，判断它是否有环。
样例
给出 -21->10->4->5, tail connects to node index 1，返回 true

class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next



class Solution:

    def hasCycle(self, head):
        fast = head
        slow = head
        while true:
            if fast.next:
                fast = fast.next.next
                slow = slow.next
                if not fast and not slow:
                    return False
                elif fast == slow:
                    return True
            else:
                return False
        return False

链表排序
在 O(n log n) 时间复杂度和常数级的空间复杂度下给链表排序。
样例
给出 1->3->2->null，给它排序变成 1->2->3->null.
不会做!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
刷完排序再回头看这道题!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next



class Solution:
   
    def sortList(self, head):
        # write your code here

"""






if __name__ == '__main__':
    a = ListNode(1)
    b = ListNode(3)
    c = ListNode(5)
    d = ListNode(8)
    e = ListNode(2)
    f = ListNode(1)
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = None 
    head = Solution().hasCycle(a)
    print(head)
    """
    if head:
        print(head)
    else:
        print('head is None')
    while head:
        print(head.val)
        head = head.next
        """







