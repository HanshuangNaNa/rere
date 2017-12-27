#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: HansHuang
# Created Time : 2017年12月27日 星期三 17时15分22秒
# File Name: review.py
# Description:
"""
import logging
logging.basicConfig(level=logging.INFO,format='%(asctime)s %(filename)s : %(levelname)s %(message)s',datefmt='%Y-%m-%d %A %H:%M:%S')

#二分查找
def BinarySearch(alist,target):
    left,right = 0,len(alist)-1
    while left <= right:
        mid = (left+right) // 2
        if alist[mid] == target:
            return mid
        elif alist[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

#最长上升连续子序列
def longSequence(alist):
  
    length,longest = 0,0
    for index,value in enumerate(alist):
        if index == 0 or alist[index] < alist[index-1]:
            length = 1
        else:
            length = length + 1
        longest = max(longest,length)
    return longest

def longhelp(alist):
    return max(longSequence(alist),longSequence(list(reversed(alist))))




if __name__ == '__main__':
    alist = [1,2,3,4,5,6,7,8,9]
    print(longSequence(alist))
