# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 20:13:44 2019

@author: yllzxzyq
"""

n,a,b,c,f=map(int,input().split(' '))
def Q(f,a,b,c,i):
    if i<0:
        return 0
    elif i==0:
        return f
    else:
        return a*Q(f,a,b,c,i-1)+b*Q(f,a,b,c,i-2)+c*Q(f,a,b,c,i-3)+2*i**2-i+32767
x=Q(f,a,b,c,n)%1000000007