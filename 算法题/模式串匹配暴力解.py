# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 20:06:37 2019

@author: yllzxzyq
"""

str1=input("mode:")
str2=input("pattern:")
def se(str1,str2):
    if len(str1)-len(str2)<0:
        return False
    for i in range(len(str1)-len(str2)+1):
        j=0
        while j<len(str2):
            if str1[i+j]==str2[j]:
                j+=1
            else:
                break
        if j==len(str2):
            return True
    return False