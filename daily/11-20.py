#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: HansHuang
# Created Time : 2017年11月20日 星期一 12时20分00秒
# File Name: daily.py
# Description:
"""
import logging
logging.basicConfig(level=logging.INFO,format='%(asctime)s %(filename)s : %(levelname)s %(message)s',datefmt='%Y-%m-%d %A %H:%M:%S')
"""
删除元素
给定一个数组和一个值，在原地删除与值相同的数字，返回新数组的长度。
元素的顺序可以改变，并且对新的数组不会有影响。
样例
给出一个数组 [0,4,4,0,0,2,4,4]，和值 4
返回 4 并且4个元素的新数组为[0,0,0,2]

class Solution:

    def removeElement(self, A, elem):
        left = 0
        for num in elem:
            if num != A:
                elem[left] = num
                left += 1

        return left

子数组之和 
给定一个整数数组，找到和为零的子数组。你的代码应该返回满足要求的子数组的起
始位置和结束位置
注意事项
There is at least one subarray that it's sum equals to zero.
样例
给出 [-3, 1, 2, -3, 4]，返回[0, 2] 或者 [1, 3]


class Solution:
    #暴力双for循环 
    def subarraySum(self, nums):
        for left in range(len(nums)-1):
            sums = 0
            sums = nums[left]
            for right in range(left+1,len(nums)):
                sums = sums + nums[right]
                if sums == 0:
                    return [left,right]
        return None

恢复旋转排序数组
给定一个旋转排序数组，在原地恢复其排序。
说明
什么是旋转数组？
比如，原始数组为[1,2,3,4], 则其旋转数组可以是[1,2,3,4], [2,3,4,1], [3,4,1,2], [4,1,2,3]
样例
[4, 5, 1, 2, 3] -> [1, 2, 3, 4, 5]

class Solution:

    def recoverRotatedSortedArray(self, nums):
        for index in range(len(nums)):
            if nums[index] > nums[index+1]:
                break
        return reversed(list(reversed(nums[:index+1]))+list(reversed(nums[index+1:])))

搜索插入位置


给定一个排序数组和一个目标值，如果在数组中找到目标值则返回索引。如果没有，返回到它将会被按顺序插入的位置。
你可以假设在数组中无重复元素。
样例
[1,3,5,6]，5 → 2
[1,3,5,6]，2 → 1
[1,3,5,6]， 7 → 4
[1,3,5,6]，0 → 0


class Solution:

    def searchInsert(self, A, target):
        left = 0
        right = len(A) - 1
        while left < right:
            mid = (left + right) // 2
            if target > A[mid]:
                left = mid + 1
            elif target < A[mid]:
                right = mid - 1
            else:
                return mid
        print(left)
        if A[left] > target:
            return left
        else:
            return left + 1 

搜索区间
给定一个包含 n 个整数的排序数组，找出给定目标值 target 的起始和结束位置。
如果目标值不在数组中，则返回[-1, -1]
样例
给出[5, 7, 7, 8, 8, 10]和目标值target=8,
返回[3, 4]
"""
class Solution:
    """
    @param: A: an integer sorted array
    @param: target: an integer to be inserted
    @return: a list of length 2, [index1, index2]
    """
    def searchRange(self, A, target):
        found = False
        left = 0
        right = len(A) - 1
        while left < right:
            if A[left] == target and A[right] == target:
                return [left,right]
            elif A[(left+right)//2] > target:
                right = (left+right)//2
            elif A[(left+right)//2] < target:
                left = (left+right) // 2
        return [-1,-1]

    def standard(self,A,target):
        ret = [-1,-1]
        if not A:
            return ret

        st,ed = 0,len(A) - 1
        while st + 1 < ed:
            mid = (st+ed) / 2
            if A[mid] == target:
                ed = mid
            elif A[mid] < target:
                st = mid
            else:
                ed = mid
        if A[st] == target:
            ret[0] = st
        elif A[ed] == target:
            ret[0] == ed
        st, ed = 0, len(A) -1

        while st + 1< ed:
            mid = (st+ed) / 2
            if A[mid] ==target:
                st = mid
            elif A[mid] < target:
                st = mid
            else:
                ed = mid
        if A[ed] ==target:
            ret[1] = ed
        elif A[st] == target:
            ret[1] == st
        return ret

if __name__ == '__main__':
    s = Solution()
    print(s.searchRange([1,2,2,3,4,5,7,8,9],2)) 
