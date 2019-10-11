# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 10:07:51 2019

@author: yllzxzyq
"""
n=int(input())
str=input()
tag,sum1=0,0
for i in range(n):
    if str[i]<'a'and tag==0:
        if i+1<n and str[i+1]<'a':
            tag=1
        sum1+=1
    elif str[i]>='a' and tag==1:
        if i+1<n and str[i+1]>='a':
            tag=0
        sum1+=1
print(sum1+n)