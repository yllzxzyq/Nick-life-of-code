# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 17:22:33 2019

@author: yllzxzyq
"""

def multiply(num1: str, num2: str) -> str:
        if len(num1)<len(num2):
            num1,num2=num2,num1
        if num1=='0' or num2=='0':
            return 0
        L=[]
        
        for i in range(len(num2)):
            l=''
            tag=0
            for j in range(1,len(num1)+1):
                r=tag+int(num2[i])*int(num1[-j])
                tag=r//10
                l=str(r%10)+l
            l=str(tag)+l
            L.append(int(l)*10**(len(num2)-i-1))
        return str(sum(L))
    
x=multiply('29','29')
print(x)