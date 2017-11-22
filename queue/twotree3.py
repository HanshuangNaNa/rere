#!/usr/bin/env python3
# -*- coding=utf8 -*-
"""
# Author: Hans
# Created Time : 2017年10月27日 星期五 12时03分56秒
# File Name: twotree3.py
# Description:
给出一棵二叉树，返回其节点值的锯齿形层次遍历（先从左往右，下一层再从右往左，层与层之间交替进行） 
您在真实的面试中是否遇到过这个题？
给出一棵二叉树 {3,9,20,#,#,15,7},
    3
   / \
  9  20
    /  \
   15   7
返回其锯齿形的层次遍历为：
[
  [3],
  [20,9],
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
    @return: A list of lists of integer include the zigzag level order traversal of its nodes' values.
    """
    #我的答案
    def getlist(TreeNode):
        p,level,alist = [],1,[]
        p.append(TreeNode)
        alist.append(TreeNode)
        while len(p) != 0:
            q = []
            for node in p:
                if level % 2 == 0:
                    q.append(node.left)
                    q.append(node.right)
                else:
                    q.append(node.right)
                    q.append(node.left)
                level = level + 1
            alist.appendi(q)
            p=q
        return alist

    #递归版本
    def preorder(self,root,level,res):
        if root:
            if len(res) < level+1:
                res.append([])
            if level % 2 == 0:
                res[level].eppend(root.val)
            else:
                res[level].insert(0,root.val)
            self.preorder(root.left,level+1,res)
            self.preorder(root.right,level+1,res)

    def zigzagLevelOrder(self,root):
        self.results = []
        self.preorder(root,0,self.results)
        return self.results
