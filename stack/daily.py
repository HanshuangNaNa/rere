#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: HansHuang
# Created Time : 2017年11月03日 星期五 22时28分27秒
# File Name: daily.py
# Description:
实现一个带有取最小值min方法的栈，min方法将返回当前栈中的最小值。
你实现的栈将支持push，pop 和 min 操作，所有操作要求都在O(1)时间内完成。
如果堆栈中没有数字则不能进行min方法的调用
如：
h(1)，pop()，push(2)，push(3)，min()， push(1)，min() 返回 1，2，1

class MinStack:

    #gparam: a: An integer

    def __init__(self, a):
        # do intialization if necessary
        self.stack = []
        self.minstack = []

    #gparam: number: An integer
    #greturn: nothing
    def push(self, number):
        # write your code here
        self.stack.append(number)
        if len(self.minstack) == 0 or number < self.minstack[-1]:
            self.minstack.pop()
            self.minstack.append(number)

    #greturn: An integer
    def pop(self):
        # write your code here
        if self.stack[-1] == self.minstack[-1]:
            self.minstack.pop()
        return self.stack.pop()

    #greturn: An integer
    def min(self):
        # write your code here
        return self.minstack[-1]
给定一个字符串所表示的括号序列，包含以下字符： '(', ')', '{', '}', 
'[' and ']'， 判定是否是有效的括号序列。
样例
括号必须依照 "()" 顺序表示， "()[]{}" 是有效的括号，但 "([)]"则是无效的括号。
class Solution:
 
    #gparam: s: A string
    #greturn: whether the string is a valid parentheses

    def isValidParentheses(self, s):
        # write your code here
        stack = []
        Flag = True
        for char in s:
            if char not in '({[' and len(stack) == 0:
                Flag = False
                return Flag
            else:
                stack.append(char)
            if char == ')' and stack[-1] == '(' or char == '}' and stack[-1] == '{' or char ==']' and stack[-1] == '[':
                stack.pop()
            else:
                Flag = False
        return Flag

        
"""
"""
#标准答案
def isVP(self,s):
    stack = []
    for ch in s:
        if ch == '(' or ch == '{' or ch == '[':
            stack.append(ch)
        else:
            if not stack:
                return False
            if ch == ']' and stack[-1] != '[' or ch == ')' and stack[-1] != '(' or ch == '}' and stack[-1] != '{':
                return False
            stack.pop()

    return not stack
"""
"""
求逆波兰表达式的值。
在逆波兰表达法中，其有效的运算符号包括 +, -, *, / 。每个运算对象可以是整数，也可以是另一个逆波兰计数表达。
样例
["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6
"""
"""
class Solution:

    #param: tokens: The Reverse Polish Notation
    #return: the value
 

    def evalRPN(self, tokens):
        # write your code here
        stack = []
        for ch in tokens:
            if ch not in '+-*/':
                stack.append(ch)
            else:
                temp1 = int(stack.pop())
                temp2 = int(stack.pop())
                if ch == '+':
                    stack.append(temp2+temp1)
                elif ch == '-':
                    stack.append(temp2-temp1)
                elif ch =='*':
                    stack.append(temp1*temp2)
                else:
                    stack.append(temp2/temp1)
        return stack[0]

a = ["2", "1", "+", "3", "*"]
s = Solution()
s.evalRPN(a)
"""
"""
给定一个文档(Unix-style)的完全路径，请进行路径简化。
样例
"/home/", => "/home"

"/a/./b/../../c/", => "/c"
"""
"""
class Solution:
    # @param path, a string
    # @return a string
    def simplifyPath(self, path):
        stack = []
        i = 0
        res = ''
        while i < len(path):
            end = i+1
            while end < len(path) and path[end] != "/":
                end += 1
            sub=path[i+1:end]
            if len(sub) > 0:
                if sub == "..":
                    if stack != []:
                        print('now pop:'+stack.pop())
                        print(stack)
                elif sub != ".":
                    stack.append(sub)
                    print('now append:'+sub)
                    print(stack)
            i = end
        if stack == []: return "/"
        for i in stack:
            res += "/"+i
        return res
"""
"""
给你一个嵌套的列表，实现一个迭代器将其摊平。
一个列表的每个元素可能是整数或者一个列表。

 注意事项

You don't need to implement the remove method.

样例
给出列表 [[1,1],2,[1,1]]，经过迭代器之后返回 [1,1,2,1,1]。

给出列表 [1,[4,[6]]]，经过迭代器之后返回 [1,4,6]。
"""
"""
This is the interface that allows for creating nested lists.
You should not implement it, or speculate about its implementation

class NestedInteger(object):
    def isInteger(self):
        # @return {boolean} True if this NestedInteger holds a single integer,
        # rather than a nested list.

    def getInteger(self):
        # @return {int} the single integer that this NestedInteger holds,
        # if it holds a single integer
        # Return None if this NestedInteger holds a nested list

    def getList(self):
        # @return {NestedInteger[]} the nested list that this NestedInteger holds,
        # if it holds a nested list
        # Return None if this NestedInteger holds a single integer
"""
"""
未完成
class NestedIterator(object):

    def __init__(self, nestedList):
        # Initialize your data structure here.

    # @return {int} the next element in the iteration
    def next(self):
        # Write your code here

    # @return {boolean} true if the iteration has more element or false
    def hasNext(self):
        # Write your code here


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())

"""
"""
在经典的汉诺塔问题中，有 3 个塔和 N 个可用来堆砌成塔的不同大小的盘子。要求盘子必须按照从小到大的顺序从上往下堆 （如，任意一个盘子，其必须堆在比它大的盘子上面）。同时，你必须满足以下限制条件：
(1) 每次只能移动一个盘子。
(2) 每个盘子从堆的顶部被移动后，只能置放于下一个堆中。
(3) 每个盘子只能放在比它大的盘子上面。
请写一段程序，实现将第一个堆的盘子移动到最后一个堆中。
"""
class Tower:
    """
    @param: i: An integer from 0 to 2
    """
    def __init__(self, i):
        # create three towers
        self.disks = []

    """
    @param: d: An integer
    @return: nothing
    """
    def add(self, d):
        # Add a disk into this tower
        if len(self.disks) > 0 and self.disks[-1] <= d:
            print "Error placing disk %s" % d
        else:
            self.disks.append(d)

    """
    @param: t: a tower
    @return: nothing
    """
    def moveTopTo(self, t):
        # Move the top disk of this tower to the top of t.

    """
    @param: n: An integer
    @param: destination: a tower
    @param: buffer: a tower
    @return: nothing
    """
    def moveDisks(self, n, destination, buffer):
        # Move n Disks from this tower to destination by buffer tower

    """
    @return: Disks
    """
    def getDisks(self):
        # write your code here
        return self.disks

"""
Your Tower object will be instantiated and called as such:
towers = [Tower(0), Tower(1), Tower(2)]
for i in xrange(n - 1, -1, -1): towers[0].add(i)
towers[0].move_disks(n, towers[2], towers[1])
print towers[0], towers[1], towers[2]
"""



if __name__ == '__main__':
    s = Solution()
    demo = '/a/./b/../../c/'
    demo2 ='/home/'
    print(s.simplifyPath(demo))
