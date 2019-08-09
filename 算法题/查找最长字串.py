# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 10:05:12 2019

@author: yllzxzyq
"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        d={}
        lis=[]
        for i in range(len(s)):
            j=1
            if(s[i] not in lis):
                lis.append(s[i])
                while s[-j]!=s[i]:
                    j+=1
                if(j<len(s) and s[-j]==s[i]):
                    d[s[i]]=[i,j]
        l=[0,0]
        m=0
        for x in d.values():
            if(len(s)-x[0]-x[1]>m):
                m=len(s)-x[0]-x[1]
                l=[x[0],x[1]]
        if(l[1]==1):
            return s[l[0]:]
        else:
            return s[l[0]:-l[1]+1]
