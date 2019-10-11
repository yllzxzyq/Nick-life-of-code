# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 00:17:58 2019

@author: yllzxzyq
"""
import numpy as np
from math import *
import matplotlib.pyplot as plt

#读文件部分
j= open(r"C:\Users\yllzxzyq\Desktop\t\tide.txt","r")
v= open(r"C:\Users\yllzxzyq\Desktop\t\velocity.txt","r")
jlist = []
vlist = []
for line in j.readlines():
    jlist.append(float(line.split(',')[2]))
for line in v.readlines():
    vlist.append(float(line.split('：')[1]))

num = len(jlist)
X = sum(jlist)/num

#创建B,L矩阵并计算X矩阵
B = np.ones((num,17))
for j in range(len(jlist)):
    for i in range(len(vlist)):
        B[j][2*i+1] = cos(vlist[i]*j)
        B[j][2*i+2] = sin(vlist[i]*j)
B = np.matrix(B)
L = np.matrix(jlist).T
X =(B.T*B).I*B.T*L

#误差分析
R= open(r"C:\Users\yllzxzyq\Desktop\t\RESUIT.txt","w")
for i in X.tolist():
    R.write(str(i[0])+'\n')
R.close
delta=B*X-L
H=(B*X).tolist()
rmax=max(abs(delta))
rmin=min(abs(delta))
r=open(r"C:\Users\yllzxzyq\Desktop\t\recity.txt","w")
r.write('最大误差值：'+str(rmax.tolist()[0][0])+'\n')
r.write('最小误差值：'+str(rmin.tolist()[0][0])+'\n')
sum1=0
sum2=0
for i in delta:
    sum1+=i[0]**2
    sum2+=abs(i[0])
s=sqrt(sum1/num)
mean=sum2/num
r.write('平均误差：'+str(mean.tolist()[0][0])+'\n')
r.write('平差中误差：'+str(s)+'\n')
r.close

#结果可视化
plt.figure(1) 
plt.plot(range(num),H)
plt.figure(2)
plt.plot(range(num),delta.tolist())
plt.show() 
