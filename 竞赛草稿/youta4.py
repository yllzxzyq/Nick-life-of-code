n=int(input())
L=[]
for i in range(n):
    L.append(input().split())
for j in L:
    s=j[0]
    m=int(j[1])
    pa=[]
    for x in range(m):
        pa.append(j[2+x])
    l,r=0,0
    start=0
    mid=[]
    if len(mid)<m and r<len(s):
        while s[l:r+1] not in pa and r<len(s):
            r+=1
        if s[l:r+1] in pa:
            l=r
            start=l
        else:
            l+=1
            r=l