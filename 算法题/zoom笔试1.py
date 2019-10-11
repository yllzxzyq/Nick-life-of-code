# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 15:19:30 2019

@author: yllzxzyq
"""
import copy
from typing import List, Any, Union

A = [100, 20, 100000]
c, a, b = int(A[0]), int(A[1]), int(A[2])
i = a
num = 0
while i <= b:
    L = []
    x = copy.deepcopy(i)
    j = 0
    while x/10**j > 0:
        L.append(x % (10**j)/10**(j-1))
        x = x-x % (10**j)
        j += 1
    f = 0
    for y in L:
        f += y**3
    if (f*c) == i:
        num += 1
    i += 1
print(num)
