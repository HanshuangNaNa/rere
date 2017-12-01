#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: HansHuang
# Created Time : 2017年11月27日 星期一 10时42分38秒
# File Name: daily.py
# Description:
"""
import logging
logging.basicConfig(level=logging.INFO,format='%(asctime)s %(filename)s : %(levelname)s %(message)s',datefmt='%Y-%m-%d %A %H:%M:%S')

class TreeNode:

    def __init__(self, val):

        self.val = val

        self.left, self.right = None, None
"""
二叉树的前序遍历 
给出一棵二叉树，返回其节点值的前序遍历。
样例
给出一棵二叉树 {1,#,2,3},
   1
    \
     2
    /
   3
返回 [1,2,3].



class Solution:
    #前序遍历递归
    def preorderTraversal(self, root):
        if root == None:
            return []
        return [root.val] +self.preorderTraversal(root.left) + self.preorderTraversal(root.right)

    #前序遍历迭代,使用辅助栈
    def diedai(self,root):
        if root is None:
            return []

        result = []
        stack = []
        stack.append(root)
        while stack:
            root = stack.pop()
            result.append(root.val)
            if root.right:
                stack.append(root.right)
            if root.left:
                stack.append(root.left)
        return result

    #中序遍历递归
    def inorderTraversal(self,root):
        if not root:
            return []
        else:
            return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)

    #中序遍历迭代,使用辅助栈
    def middiedai(self,root):
        if not root:
            return []
        result = []
        stack = []
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = s.pop()
                result.append(root.val)
                root = root.right
    
    #后序递归遍历
    def PostorderTraversal(self,root):
        if not root:
            return []
        else:
            return self.PostorderTraversal(root.left) + self.PostorderTraversal(root.right) + [root.val]

    #后序迭代
    def heardiedai(self,root):
        if not root:
            return []
        stack = [root]
        result = []
        prev = None
        while stack:
            curr = stack[-1]
            noChild = not curr.left and not curr.right
            childVisited = prev and (curr.left == prev or curr.right == prev)
            if noChild or childVisited:
                result.append(curr.val)
                stack.pop()
                prev = curr
            else:
                if curr.right:
                    stack.append(curr.right)
                if curr.left:
                    stack.append(curr.left)

二叉树的层次遍历 
给出一棵二叉树，返回其节点值的层次遍历（逐层从左往右访问）
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




class Solution:

    def levelOrder(self, root):
        print(root)
        result = []
        stack = [] 
        stack.append(root)
        while stack:
            result.append([node.val for node in stack])
            temp = []
            for node in stack:
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            stack = temp
        return result


二叉树的层次遍历 II
给出一棵二叉树，返回其节点值从底向上的层次序遍历（按从叶节点所在层到根节点所在的层遍历，然后逐层从左往右遍历）
样例
给出一棵二叉树 {3,9,20,#,#,15,7},

    3
   / \
  9  20
    /  \
   15   7
按照从下往上的层次遍历为：

[
  [15,7],
  [9,20],
  [3]
]


class Solution:
   
    def levelOrderBottom(self, root):
        pass

二叉树的最大深度


给定一个二叉树，找出其最大深度。
二叉树的深度为根节点到最远叶子节点的距离。
样例
给出一棵如下的二叉树:

  1
 / \ 
2   3
   / \
  4   5

这个二叉树的最大深度为3.


class Solution:
    """
    @param root: The root of binary tree.
    @return: An integer
    """
    #暴力版本
    def maxDepth(self, root):
        count = 0
        stack = [root]
        while stack:
            count += 1
            temp = []
            for node in stack:
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            stack = temp
        return count

    #试一下递归
    def digui(self,root):
        if root is None:
            return 0
        return max(self.digui(root.left),self.digui(root.right)) + 1

平衡二叉树
给定一个二叉树,确定它是高度平衡的。对于这个问题,一棵高度平衡的二叉树的定义是：一棵二叉树中每个节点的两个子树的深度相差不会超过1。 
样例
给出二叉树 A={3,9,20,#,#,15,7}, B={3,#,20,15,7}

A)  3            B)    3 
   / \                  \
  9  20                 20
    /  \                / \
   15   7              15  7

二叉树A是高度平衡的二叉树，但是B不是

""" 

class Solution:
 
    def isBalanced(self, root):
        pass
  
if __name__ == '__main__':
    a = TreeNode(3)
    b = TreeNode(9)
    c = TreeNode(20)
    d = TreeNode(15)
    e = TreeNode(7)
    a.left = b
    a.right = c
    c.left = d
    c.right = e
    s = Solution()
    logging.info(s.maxDepth(a))
