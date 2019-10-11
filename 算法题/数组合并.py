# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 14:48:31 2019

@author: yllzxzyq
"""


def merge( intervals) :
    n = len(intervals)
    if n == 0:
        return []
    intervals.sort(key=lambda x: x[0])
    l = [intervals[0]]
    for i in range(1, n):
        if l[-1][1] >= intervals[i][0]:
            l[-1][1] = max(l[-1][1], intervals[i][-1])
        else:
            l.append(intervals[i])
    return l

n,m = map(int,input().split())
door = []
for i in range(n):
    door.append(list(map(int,input().split())))

ball = []
for j in range(m):
    ball.append(int(input()))
Door = merge(door)
re = 0
for i in ball:
    for v in Door:
        if i >= v[0] and i <= v[1]:
            re+=1
            break
print(re)
