# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 21:52:53 2019

@author: keai
"""
import numpy as np

n=4
m=3
L=np.array(np.arange(1,n*m+1)).reshape(m,n)
print(L)
R=[]
def ju(l,r,L,Re):
    x1,y1=l[0],l[1]
    x2,y2=r[0],r[1]
    for i in range(x1,x2):
        Re.append(L[y1][i])
    for i in range(y1,y2):
        Re.append(L[i][x2])
    for i in range(x1,x2):
        Re.append(L[y2][x1+x2-i])
    for i in range(y1,y2):
        Re.append(L[y1+y2-i][x1])
    return Re
lt=[0,0]
rl=[len(L[0])-1,len(L)-1]
while rl[0]>lt[0] and rl[1]>lt[1]:
    R=ju(lt,rl,L,R)
    lt[0]+=1
    lt[1]+=1
    rl[0]-=1
    rl[1]-=1
if lt[0]==rl[0]:
    for i in range(lt[1],rl[1]+1):
        R.append(L[i][rl[0]])
else:
    for i in range(lt[0],rl[0]+1):
        R.append(L[rl[1]][i])

print(np.array(R))