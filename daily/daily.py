#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: HansHuang
# Created Time : 2017年11月22日 星期三 10时47分55秒
# File Name: daily.py
# Description:
"""
import logging
logging.basicConfig(level=logging.INFO,format='%(asctime)s %(filename)s : %(levelname)s %(message)s',datefmt='%Y-%m-%d %A %H:%M:%S')

"""
你给出一个整数数组(size为n)，其具有以下特点：
    相邻位置的数字是不同的
    A[0] < A[1] 并且 A[n - 2] > A[n - 1]
假定P是峰值的位置则满足A[P] > A[P-1]且A[P] > A[P+1]，返回数组中任意一个峰值的位置。
注意事项
    It's guaranteed the array has at least one peak.
    The array may contain multiple peeks, find any of them.
    The array has at least 3 numbers in it.
样例
给出数组[1, 2, 1, 3, 4, 5, 7, 6]返回1, 即数值 2 所在位置, 或者6, 即数值 7 所在位置.

class Solution:
 
    def findPeak(self, A):
        for char in range(1,len(A)-1):
            if A[char-1] < A[char] and A[char] > A[char+1]:
                return char
        return None

    def standard(self,A):
        if not A:
            return -1

        l,r = 0,len(A) - 1
        while l+1< r:
            mid = l+(r-l)//2
            if A[mid] < A[mid-1]:
                r= mid
            elif A[mid] < A[mid+1]:
                l=mid
            else:
                return mid
        return mid

搜索旋转排序数组 
假设有一个排序的按未知的旋转轴旋转的数组(比如，0 1 2 4 5 6 7 可能成为4 5 6 7 0 1 2)。给定一个目标值进行搜索，如果在数组中找到目标值返回数组中的索引位置，否则返回-1。
你可以假设数组中不存在重复的元素。
样例
给出[4, 5, 1, 2, 3]和target=1，返回 2
给出[4, 5, 1, 2, 3]和target=0，返回 -1


class Solution:
        
    #时间复杂度为O(logn+logm),并且代码难看
    def search(self, A, target):
        left,right=0,len(A)-1
        while left+1<right:
            mid = (left+right) //2
            if A[mid] < A[right]:
                right = mid
            elif A[mid] > A[right]:
                left = mid
        if A[left] < A[right]:
            splitpoint = right
        else:
            splitpoint = left
        if target > A[0]:
            left,right = 0,splitpoint
        elif target < A[0]:
            left,right = splitpoint+1,len(A)-1
        else:
            return 0
        while left+1< right:
            mid=(left+right)//2
            if target == A[mid]:
                right = mid
            elif target > A[mid]:
                left = mid
            else:
                right = mid
        if target == A[left]:
            return left
        elif target == A[right]:
            return right
        else:
            return -1

寻找旋转排序数组中的最小值
假设一个旋转排序的数组其起始位置是未知的（比如0 1 2 4 5 6 7 可能变成是4 5 6 7 0 1 2）。
你需要找到其中最小的元素。
你可以假设数组中不存在重复的元素。
注意事项
You may assume no duplicate exists in the array.
样例
给出[4,5,6,7,0,1,2]  返回 0


class Solution:

    def findMin(self, nums):
        left,right = 0,len(nums)-1
        while left + 1 < right:
            mid = (left+right) // 2
            if nums[mid] > nums[right]:
                left = mid
            elif nums[mid] < nums[right]:
                right = mid
        if nums[left] < nums[right]:
            return nums[right+1]
        else:
            return nums[right]
Sqrt(x)
Implement int sqrt(int x).
Compute and return the square root of x.
Example
sqrt(3) = 1
sqrt(4) = 2
sqrt(5) = 2
sqrt(10) = 3

class Solution:

    def sqrt(self, x):
        left,right = 0,x
        while left + 1 < right:
            mid = (left+right)//2
            if mid * mid < x:
                left = mid
            elif mid * mid > x:
                right = mid
            else:
                return mid
        if left * left < x and right * right > x:
            return left

木材加工 
有一些原木，现在想把这些木头切割成一些长度相同的小段木头，需要得到的小段的数目至少为 k。当然，我们希望得到的小段越长越好，你需要计算能够得到的小段木头的最大长度。
注意事项
木头长度的单位是厘米。原木的长度都是正整数，我们要求切割得到的小段木头的长度也要求是整数。无法切出要求至少 k 段的,则返回 0 即可。
样例
有3根木头[232, 124, 456], k=7, 最大长度为114.

"""
class Solution:
    """
    @param: L: Given n pieces of wood with length L[i]
    @param: k: An integer
    @return: The maximum length of the small pieces
    """
    def woodCut(self, L, k):
        if sum(L) < k:
            return 0
        start,end = 1,max(L)
        while start + 1 < end:
            mid = (start+end) //2
            pieces_num = sum(len_i / mid for len_i in L)
            if pieces+sum < k:
                end = mid
            else:
                start = mid
        if sum(len_i / end for len_i in L) >= k:
            return end
        return start

if __name__=='__main__':
    s= Solution()
    print(s.sqrt(4))
