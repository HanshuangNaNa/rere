#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: HansHuang
# Created Time : 2017年11月12日 星期日 09时54分48秒
# File Name: data.py
# Description:
"""
#写一个冒泡
def bubbleSort(alist):
    for length in range(len(alist)-1,1,-1):
        for index in range(length):
            if alist[index] > alist[index+1]:
                alist[index+1],alist[index] = alist[index],alist[index+1]
    return alist

#写一个选择
def choosesort(alist):
    print('method done')
    for index in range(len(alist)-1,1,-1):
        temp = alist[0]
        position = 0
        for i in range(1,index+1):
            if alist[i] > temp:
                temp = alist[i]
                position = i
        alist[i],alist[position] = temp,alist[i]
    return alist

#写一个插入排序
def insertsort(alist):
    for index in range(1,len(alist)):
        temp = alist[index]
        position = index
        while position > 0 and alist[position-1] > temp:
            alist[position] = alist[position-1] 
            position = position - 1
        alist[position] = temp
    return alist

#写一个归并排序
def mergeSort(alist):
    if len(alist) > 1:
        print('split list',alist)
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]
        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0

        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i = i + 1
            else:
                alist[k] = righthalf[j]
                j = j + 1
            k = k + 1

        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            k=k+1
            i=i+1

        while j < len(righthalf):
            alist[k] = righthalf[j]
            k = k+1
            j=j+1
    print("Merging",alist)

#写一个快速排序
def quickSort(alist):
    quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
    if first < last:
        splitpoint = partition(alist,first,last)
        quickSortHelper(alist,first,splitpoint-1)
        quickSortHelper(alist,splitpoint+1,last)

def partition(alist,first,last):
    pivotvalue = alist[first]

    leftmark = first+1
    rightmark = last

    done = False
    while not done:
        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark = leftmark + 1

        while alist[rightmark] >= pivotvalue and rightmark >=leftmark:
            rightmark = rightmark + 1

        if rightmark < leftmark:
            done = True
        else:
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp

    temp = alist[first]
    alist[first] = alist[rightmark]
    alist[rightmark] = temp

    return rightmark



if __name__ == '__main__':
    alist=[1,7,3,8,56,4,9,5,43,656]
    print(mergeSort(alist))
