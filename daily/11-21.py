#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: HansHuang
# Created Time : 2017年11月21日 星期二 11时23分57秒
# File Name: daily.py
# Description:
"""
import logging
logging.basicConfig(level=logging.INFO,format='%(asctime)s %(filename)s : %(levelname)s %(message)s',datefmt='%Y-%m-%d %A %H:%M:%S')
"""
第一个错误的代码版本 
代码库的版本号是从 1 到 n 的整数。某一天，有人提交了错误版本的代码，因此造成自身及之后版本的代码在单元测试中均出错。请找出第一个错误的版本号。
你可以通过 isBadVersion 的接口来判断版本号 version 是否在单元测试中出错，具体接口详情和调用方法请见代码的注释部分。
注意事项
请阅读上述代码，对于不同的语言获取正确的调用 isBadVersion 的方法，比如java的调用方式是SVNRepo.isBadVersion(v)
样例
给出 n=5
调用isBadVersion(3)，得到false
调用isBadVersion(5)，得到true
调用isBadVersion(4)，得到true
此时我们可以断定4是第一个错误的版本号

"""
"""
class SVNRepo:
    @classmethod
    def isBadVersion(cls, id)
        # Run unit tests to check whether verison `id` is a bad version
        # return true if unit tests passed else false.
You can use SVNRepo.isBadVersion(10) to check whether version 10 is a 
bad version.



class Solution:
  
    def binary_search(self, array,target):
        if not array:
            return -1
        start,end = 0,len(array) - 1
        while start + 1 < end:
            mid = (start+end) // 2
            if array[mid] == target:
                start = mid
            elif array[mid] < target:
                start = mid
            else:
                end = mid
        if array[start] == target:
            return start
        if array[end] == target:
            return end
        return -1

    def standard(self,nums,target):
        left = 0
        right = len(nums) - 1
        while left+1 < right:
            mid = (left + right)//2
            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                left = mid
            else:
                right = mid
        if nums[left] == target:
            return left
        if nums[right] == target:
            return right
        return -1


搜索二维矩阵
写出一个高效的算法来搜索 m × n矩阵中的值。
这个矩阵具有以下特性：
    每行中的整数从左到右是排序的。
    每行的第一个数大于上一行的最后一个整数。
样例
考虑下列矩阵：
[
  [1, 3, 5, 7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
给出 target = 3，返回 true

class Solution:

    def searchMatrix(self, martix, target):
        left = 0
        right = len(martix) - 1
        res = []
        while left + 1 < right:
            mid = (left+right) // 2
            if target < martix[mid][0]:
                right = mid
            elif target > martix[mid][-1]:
                left = mid
            elif target >= martix[mid][0] and target <= martix[mid][-1]:
                res = martix[mid]
                break
        if not res and target < martix[right][-1] and target > martix[right][0]:
            res = martix[left]
        elif not res and target < martix[left][-1] and target > martix[right][0]:
            res = martix[right]
        else:
            return False
        left,right = 0,len(res)
        while left + 1 < right:
            mid = (left+right)//2
            if res[mid] == target:
                return True
            elif res[mid] > target:
                right = mid
            else:
                left = mid
        print(left,right)
        return res[left] == target and res[right] == target

搜索二维矩阵 II 
写出一个高效的算法来搜索m×n矩阵中的值，返回这个值出现的次数。
这个矩阵具有以下特性：
每行中的整数从左到右是排序的。
每一列的整数从上到下是排序的。
在每一行或每一列中没有重复的整数。
样例
考虑下列矩阵：
[

    [1, 3, 5, 7],

    [2, 4, 7, 8],

    [3, 5, 9, 10]
]
给出target = 3，返回 2
"""
class Solution:
    """
    @param: matrix: A list of lists of integers
    @param: target: An integer you want to search in matrix
    @return: An integer indicate the total occurrence of target in the given matrix
    """
    def searchMatrix(self, matrix, target):
        if not matrix or not matrix[0]:
            return 0
        occur = 0
        row,col = 0,len(matrix[0])-1
        while row < len(matrix) and col >= 0:
            if matrix[row][col] == target:
                occur += 1
                col -= 1
            elif matrix[row][col] < target:
                row += 1
            else:
                col -= 1
        return occur



if __name__ == '__main__':
    s = Solution()
    print(s.searchMatrix([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]],17))
        
