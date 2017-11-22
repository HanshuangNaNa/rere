#!/usr/bin/env python3
# -*- coding=utf8 -*-
"""
# Author: Hans
# Created Time : 2017年10月27日 星期五 11时01分16秒
# File Name: twotree.py
# Description:
给出一棵二叉树，返回其节点值的层次遍历（逐层从左往右访问）
您在真实的面试中是否遇到过这个题？
样例
给一棵二叉树 {3,9,20,#,#,15,7} ：
  3
 / \
9  20
  /  \
 15   7
返回他的分层遍历结果：
[
  [3],
  [9,20],
  [15,7]
]
"""
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    """
    @param: root: A Tree
    @return: Level order a list of lists of integer
    """
    def levelOrder(self, root):
        # write your code here
        self.results = []
        q = [root]
        while q:
            new_q = []
            self.result.append([n.val for n in q])
            for node in q:
                if node.left != None:
                    new_q.append(node.left)
                if node.right != None:
                    new_q.append(node.right)
            q = new_q
        return self.results
