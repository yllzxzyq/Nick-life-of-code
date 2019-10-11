# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 21:09:37 2019

@author: keai
"""
nums=[1,2,3,4]
L=[]
def son(i,r,nums,L):
    if i == len(nums):
        L.append(r.copy())
        return
    son(i+1,r,nums,L)
    son(i+1,r+[nums[i]],nums,L)
son(0,[],nums,L)
print(L)