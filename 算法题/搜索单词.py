# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 23:29:32 2019

@author: keai
"""

def searchword(i,j,n,L,r):
    if board[i][j]==word[n] and len(L)<len(word):
        L.append([i,j])
        if len(L)==len(word):
            r=L
            return
        board[i][j]=' '
        if i>0:
            searchword(i-1,j,n+1,L,r)
        if i<len(board)-1:
            searchword(i+1,j,n+1,L,r)
        if j>0:
            searchword(i,j-1,n+1,L,r)
        if j<len(board[0])-1:
            searchword(i,j+1,n+1,L,r)
        

board = [["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]]
word = "ABCEFSADEESE"
re,r=[],[]
searchword(0,0,0,re,r)