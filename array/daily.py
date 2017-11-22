#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: HansHuang
# Created Time : 2017年11月14日 星期二 09时55分24秒
# File Name: daily.py
# Description:
二分查找
给定一个排序的整数数组（升序）和一个要查找的整数target，用O(logn)的时间查找到target第一次出现的下标（从0开始），如果target不存在于数组中，返回-1。
样例
在数组 [1, 2, 3, 3, 4, 5, 10] 中二分查找3，返回2。

class Solution:
    def binarySearch(self, nums, target):
        # write your code here
        left, right = 0, len(nums)
        while left + 1 < right :
            mid = (left + right) // 2
            if nums[mid] < target :
                left = mid
            else:
                right = mid
        if nums[left] == target :
            return left
        elif nums[right] == target :
            return right
        return -1;

最长上升连续子序列
给定一个整数数组（下标从 0 到 n-1， n 表示整个数组的规模），请找出该数组中的最长上升连续子序列。（最长上升连续子序列可以定义为从右到左或从左到右的序列。）
给定 [5, 4, 2, 1, 3], 其最长上升连续子序列（LICS）为 [5, 4, 2, 1], 返回 4.
给定 [5, 1, 2, 3, 4], 其最长上升连续子序列（LICS）为 [1, 2, 3, 4], 返回 4.
"""
class Solution:
    #自己写的,想在一个函数里解决,但是好像有些问题 
    def longestIncreasingContinuousSubsequence(self, A):
        stack = [0,]
        flag = True
        count = 1
        i = 0
        while i < len(A)-1:
            while flag and i < len(A)-1:
                if A[i] > A[i+1]:
                    flag = False
                    if count > stack[-1]:
                        print('count:',count)
                        stack.pop()
                        stack.append(count)
                else:
                    count = count + 1
                    i = i + 1
                    print('死循环了吗')
                    print(count)
            while not flag and i < len(A)-1:
                if A[i] < A[i+1]:
                    flag = True
                    if count > stack[-1]:
                        stack.pop()
                        stack.append(count)
                else:
                    count = count + 1
                    i = i + 1
        return stack[-1]

    #标准答案
    def standard(self,A):
        length,longest = 0,0
        for index,a in enumerate(A):
            if index == 0 or A[index] < A[index - 1]:
                length = 1
            else:
                length = length + 1
            longest = max(longest,length)
        return longest

    def getLongest(self,A):
        return max(self.standard(A),self.standard(list(reversed(A))))


if __name__ == '__main__':
    alist=[1,2,3,4,5,6,7,8,9]
    s = Solution()
    print(s.longestIncreasingContinuousSubsequence(alist))
  
