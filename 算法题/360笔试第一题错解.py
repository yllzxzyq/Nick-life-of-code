# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 16:23:11 2019

@author: yllzxzyq
"""
N,M=map(int,input().split(" "))
L=[]
reN=[]
for i in range(N):
    line=list(map(int,input().split(" ")))
    reN.append(max(line))
    L.append(line)
    
reM=[]
for j in range(M):
    m=0
    for i in range(N):
        if m<=L[i][j]:
            m=L[i][j]
    reM.append(m)
print((sum(reM)+sum(reN)+N*M)*2)