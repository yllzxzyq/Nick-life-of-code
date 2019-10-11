# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 20:32:36 2019

@author: yllzxzyq
"""

def kmp(str1,str2):
    if len(str1)-len(str2)<0:
        return False
    i=0
    while i<len(str1)-len(str2)+1:
        j=0
        while j<len(str2):
            if str1[i+j]==str2[j]:
                j+=1
            else:
                i=i+j+1
                j=Next(j,str2)
                break
        if j==len(str2):
            return True
    return False

def Next(x,str2):
    N=[]
    for i in range(len(str2)):
        if i==0:
            N.append(-1)
            continue
        j=0
        while j<i:
            if str2[:j]==str2[i-j:i]:
                j+=1
            else:break
        N.append(j-1)
    return N[x]

s1="abcabcabc"
s2='cabc'
re=kmp(s1,s2)