#错解，没考虑t串中出现重复的情况
def minWindow(s,t):
    L=[]
    re=s
    for i in range(len(s)):
        if len(L)<2*len(t) and s[i] in t and s[i] not in L:
            L.append(s[i])
            L.append(i)
            if len(L)==2*len(t):
                re=s[L[1]:L[-1]+1]
        if len(L) > 0 and s[i] in L:
            x = L.index(s[i])
            L.append(s[i])
            L.append(i)
            L.pop(x)
            L.pop(x)
            if len(L) == 2*len(t):
                if len(re) > L[-1]- L[1]:
                    re = s[L[1]:L[-1]+1]
    if len(L)<len(t):
        return ''
    return re

#滑动窗口

s="bbaa"
t="aba"
r=minWindow(s,t)
print(r)