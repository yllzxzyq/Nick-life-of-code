# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 16:08:24 2019

@author: yllzxzyq
"""
I=list(input())
L=[]
for i in range(len(I)):
    if I[i]=='0' or I[i]=='1':
        L.append(int(I[i]))
L[0]=L[:4]
L[1]=L[4:8]
L[2]=L[8:12]
L[3]=L[12:16]
L=L[:4]
D=input().split(']')
for j in range(len(D)-2):
    x=int(D[j][-3])
    y=int(D[j][-1])
    if x-1>0:
        L[x-2][y-1]=(-1)*(L[x-2][y-1]-1)
    if y-1>0:
        L[x-1][y-2]=(-1)*(L[x-1][y-2]-1)
    if y<4:
        L[x-1][y]=(-1)*(L[x-1][y]-1)
    if x<4:
        L[x][y-1]=(-1)*(L[x][y-1]-1)
print(L)
    