# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 10:48:17 2019

@author: yllzxzyq
"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        d={}
        l=[]
        m=0
        le=len(s)
        if(le==0):
            return ''
        elif(le==1):
            return s
        else:
            for i in range(le):
                j=t=1
                while i+j<le and i-j>=0 and s[i+j]==s[i-j]:
                    j+=1
                l.append(s[i-j+1:i+j])
                while i-t>=0 and i+t-1<le and s[i+t-1]==s[i-t]:
                    t+=1
                l.append(s[i-t+1:i+t-1])
            for x in l:
                if(len(x)>m):
                    m=len(x)
                    re=x
            return re
    
    
    
class Solution:
    def longestPalindrome(self,s):
        str_length = len(s)
        max_length = 0
        start = 0
        for i in range(str_length):
            if i - max_length >= 1 and s[i - max_length - 1:i + 2] == s[i - max_length - 1:i + 2][::-1]:
                start = i - max_length - 1
                max_length += 2
                continue
            if i - max_length >= 0 and s[i - max_length:i + 2] == s[i - max_length:i + 2][::-1]:
                start = i - max_length
                max_length += 1
        return s[start:start + max_length+1]