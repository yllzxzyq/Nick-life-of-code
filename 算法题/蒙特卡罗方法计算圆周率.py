# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 17:07:36 2019

@author: yllzxzyq
"""

from random import random
from time import perf_counter

hits=0
Darts = 1000*1000
start = perf_counter()
for i in range(1,Darts+1):
    x,y = random(),random()
    dist=pow(x**2+y**2,0.5)
    if dist <=1:
        hits +=1
pi = 4*(hits/Darts)
print("圆周率是："+str(pi))
print("运行时间是：{:.5f}s".format(perf_counter()-start))