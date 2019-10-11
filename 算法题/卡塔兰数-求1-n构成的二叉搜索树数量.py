# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 09:57:26 2019

@author: keai
"""

def numTrees(n):
    L=[1,1]
    if n<=1:
        return L[n]
    for i in range(2,n+1):
        x=0
        for j in range(i):
            x+=L[j]*L[i-j-1]
        L.append(x)
    return L[-1]