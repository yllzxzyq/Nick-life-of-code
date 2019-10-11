# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 16:46:35 2019

@author: yllzxzyq
"""

m,y=list(map(int,input().split(' ')))
days=[31,28,31,30,31,30,31,31,30,31,30,31]
tag=0
if y%4==0:
    if y%100==0 and y%400!=0:
        tag=0
    else:
        tag=1
if m==2:
    print(days[m-1]+tag)
else:print(days[m-1])