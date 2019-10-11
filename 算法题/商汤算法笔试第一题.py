# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 19:32:57 2019

@author: yllzxzyq
"""

n,m=map(int,input().split(' '))
w={}
a=[]
for i in range(n):
    x,y=map(int,input().split(' '))
    w[x]=y
    a.append(x)
a.sort()
re=[]
for j in range(m):
    R=[]
    we=int(input())
    l=0
    while l<n and a[l]<we:
        l+=1
    for o in range(l,n):
        R.append(w[a[o]])
    if len(R)!=0:
        re.append(max(R))
    else:
        re.append(-1)
for p in re:
    print(p)