# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 13:54:08 2019

@author: yllzxzyq
"""

import random, operator
 
 
def GenerateRandomArray(size,start, end): # 产生一个随机数列长度为size，数字范围为-value~value
    array =[]
    for i in range(size):
        array.append(random.randint(start,end))
        #array.append((end-start)*random.random() + start)
    return array
 
 
def RightMathod(array): # 一定正确的方法：自带排序方法
    array.sort()
    return array
 
 
def IsRight(times, size, start,end, func): # 次数、长度、数字范围、测试方法
    succeed = True
    for i in range(times):
        arr1 = GenerateRandomArray(size, start, end)
        arr2 = arr1.copy()
        arr3 = arr1.copy()
        func(arr1)
        RightMathod(arr2)
        if not operator.eq(arr1, arr2):
            succeed = False
            print(arr3)
            break
    print("NICE" if succeed == True else "WRONG")
    
def pai(nums):
    for x in range(len(nums)-1):
        for i in range(len(nums)-1):
            if nums[i]>nums[i+1]:
                nums[i],nums[i+1] = nums[i+1],nums[i]
    return nums

IsRight(10000, 15, 0,100, pai)