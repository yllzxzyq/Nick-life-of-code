# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 13:02:59 2019

@author: yllzxzyq
"""

string = input()
list1 = string.split(" ")
list1.sort()
max1 = float(list1[0])*float(list1[1])*float(list1[-1])
max2 = float(list1[-3])*float(list1[-1])*float(list1[-2])
if max1>max2:
    max0=max1
else:
    max0=max2
print(max0)