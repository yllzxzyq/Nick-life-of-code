d = {}
for i in range(10):
    d[str(i)] = i
La = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
LA = []
for i in range(len(La)):
    LA.append(La[i].upper())
    d[La[i]] = 10+i
    d[La[i].upper()] = 36+i
s = input()
re = ''
l,r = 0,0
tag = 0
n = len(s)
while r < n :
    r+=1
    if d[s[l]] < 10:
        while r <= n-1 and d[s[r]]<10 and (d[s[r]]-d[s[r-1]])==1:
            r+=1
            tag+=1
    elif d[s[l]] >= 10 and d[s[l]] <= 35:
        while r <= n-1 and d[s[r]]>=10 and d[s[r]]<=35 and (d[s[r]]-d[s[r-1]])==1:
            r+=1
            tag+=1
    else:
        while r <= n-1 and d[s[r]]>=36 and (d[s[r]]-d[s[r-1]])==1:
            r+=1
            tag+=1
    if tag >=3:
        re+=s[l]+'-'+s[r-1]
    else:
        re+=s[l:r]
    tag = 0
    l = r
print(re)