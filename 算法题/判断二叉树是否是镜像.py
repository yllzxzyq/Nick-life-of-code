# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 11:28:05 2019

@author: keai
"""
#递归判断二叉树是否镜像
def isSymmetric(root):
        def helper(tree1,tree2):
            if tree1 is None and tree2 is None:
                return True
            if tree1 is None or tree2 is None:
                return False
            return tree1.val==tree2.val and helper(tree1.left,tree2.right) and helper(tree1.right,tree2.left)
        return helper(root,root)

#迭代方法判断二叉树是否镜像
