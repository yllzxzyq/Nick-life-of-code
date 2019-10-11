# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 14:45:54 2019

@author: yllzxzyq
"""
def rotate(matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        """
        方法一
        n=len(matrix)
        for i in range(n):
            for j in range(i,n):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        for i in matrix:
            i.reverse()
        """
        #方法二
        n=len(matrix)
        for i in range(n//2+n%2):
            for j in range(n//2):
                t=matrix[i][j]
                matrix[i][j]=matrix[n-j-1][i]
                matrix[n-j-1][i]= matrix[n-i-1][n-j-1]
                matrix[n-i-1][n-j-1]=matrix[j][n-i-1]
                matrix[j][n-i-1]=t
