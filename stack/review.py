#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: HansHuang
# Created Time : 2017年12月27日 星期三 21时44分02秒
# File Name: review.py
# Description:
"""
import logging
logging.basicConfig(level=logging.INFO,format='%(asctime)s %(filename)s : %(levelname)s %(message)s',datefmt='%Y-%m-%d %A %H:%M:%S')

#实现一个min/max方法的栈,O(1)时间复杂度,没有数字则没有min
class Stack:

    def __init__(self):
        self.stack = []
        self.minstack = []

    def push(self,number):
        self.stack.append(number)
        if len(self.minstack) == 0 or number <= self.minstack[-1]:
            self.minstack.append(number)

    def pop(self):
        if self.stack.pop() == self.minstack[-1]:
            self.minstack.pop()

    def min(self):
        return self.minstack[-1]

#判断是否有效序列 '(){}[]'
def isValid(s):
    stack = []
    for char in s:
        if char in '({[':
            stack.append(char)
        elif char in ')}]' and len(stack) == 0:
            return False
        elif char == ')' and stack[-1] == '(' or char == '}' and stack[-1] == '{' or char == ']' and stack[-1] == '[':
            stack.pop()
        else:
            return False
    return True



if __name__ == '__main__':
    s = ')))[](){]]][[}}}[]]]}' 
    print(isValid(s))
