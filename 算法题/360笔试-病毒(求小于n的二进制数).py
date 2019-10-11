L=[]
try:
    while 1:
        L.append(input())
except:
    pass
def R(s):
    r=0
    for i in range(len(s)):
        if int(s[i])>1:
            r+=2**(len(s)-i)-1
            break
        if int(s[i])==1:
            r+=2**(len(s)-i-1)
    return r
for i in L:
    print(R(i))


# 10
# 20-