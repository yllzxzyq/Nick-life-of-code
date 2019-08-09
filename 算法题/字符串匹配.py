# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 14:30:22 2019

@author: yllzxzyq
"""

    def isMatch(self, s: str, p: str) -> bool:
        t=True
        t=i=j=0
        while i<len(s) and j<len(p):
            if (p[j] in [s[i],'.']):
                i+=1
                t+=1
                j+=1
            elif(p[j]=='*' ):
                t+=1
                if p[j-1] in [s[i],'.']:
                    i+=1
                else:
                    j+=1
                    continue
            elif(j<len(p)-1 and p[j+1]=='*'):
                j+=2
                t+=2
            else:
                t=False
                break
        if(i==len(s) and t>=len(p)):
            return t
        else:
            return False
