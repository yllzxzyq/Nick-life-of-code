# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 15:06:15 2019

@author: keai
"""
#层次遍历二叉树
def levelOrder(root):
        Re=[]
        def level(node,le):
            if node:
                if len(Re)==le:
                    Re.append([])
                Re[le].append(node.val)
                if node.left:
                    level(node.left,le+1)
                if node.right:
                    level(node.right,le+1)
        level(root,0)
        return Re