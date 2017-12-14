#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: HansHuang
# Created Time : 2017年12月01日 星期五 10时48分29秒
# File Name: daily.py
# Description:
"""
import logging
logging.basicConfig(level=logging.INFO,format='%(asctime)s %(filename)s : %(levelname)s %(message)s',datefmt='%Y-%m-%d %A %H:%M:%S')

#冒泡排序
def Bubble(alist):
    for index in range(len(alist)-1,0,-1):
        for cur in range(index):
            if alist[cur] > alist[cur+1]:
                alist[cur+1],alist[cur] = alist[cur],alist[cur+1]
    return alist

#选择
def Selection(alist):
    for index in range(len(alist)-1,0,-1):
        logging.info('找出前{0}位最大的数'.format(index))
        temp = 0
        curvalue = alist[0]
        logging.info('此时列表:{0}'.format(alist))
        for cur in range(index+1):
            logging.info('当前位置:{0},当前值:{1}'.format(cur,alist[cur]))
            if alist[cur] > curvalue:
                logging.info('此时较大值为{0},位置{1}'.format(alist[cur],cur))
                temp = cur
                curvalue = alist[cur]
        logging.info('找到最大值{0},位置{1}'.format(alist[temp],temp))
        alist[index],alist[temp] = alist[temp],alist[index]
        logging.info('交换后:{0}'.format(alist))
    return alist

#插入
def Insert(alist):
    for index in range(1,len(alist)):
        curr = index
        currvalue = alist[curr]
        while curr > 0 and alist[curr-1] > currvalue:
            alist[curr] = alist[curr-1]
            curr = curr - 1
        alist[curr] = currvalue
    return alist

#归并排序
def MergeSort(alist):
    if len(alist) > 1:
        logging.info('split list:{0}'.format(alist))
        mid = len(alist) // 2

        left = alist[:mid]
        right = alist[mid:]
        MergeSort(left)
        MergeSort(right)
        i,j,z = 0,0,0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                alist[z] = left[i]
                i += 1
            else:
                alist[z] = right[j]
                j += 1
            z += 1
        while i < len(left):
            alist[z] = left[i]
            i+=1
            z+=1
        while j < len(right):
            alist[z] = right[j]
            j+=1
            z+=1
        logging.info('Mergeing:{0}'.format(alist))
    
#快速排序
def quickSort(alist):
    quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
    if first < last:
        splitpoint = done(alist,first,last)
        quickSortHelper(alist,first,splitpoint-1)
        quickSortHelper(alist,splitpoint+1,last)
    

def done(alist,first,last):
    currentvalue = alist[first]
    left = first + 1
    right = last
    flag = False
    count = 0
    while not flag:
        while alist[left] < currentvalue and left <= right:
            left = left + 1
        while alist[right] > currentvalue and left <= right:
            right = right - 1
        if left > right:
            flag = True
        else:
            alist[left],alist[right] = alist[right],alist[left]
    alist[first],alist[right] = alist[right],alist[first]
    return right


if __name__ == '__main__':
    a = [666,7,212,14,1,7234,66666]
    logging.info(quickSort(a))
    logging.info(a)
