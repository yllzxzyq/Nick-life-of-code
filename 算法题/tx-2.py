n = int(input())
inp = []
for i in range(n):
    x,y = map(int,input().split())
    inp.append([x,y])
inp.sort(key = lambda x:x[1])
l,r = 0,n-1
re = float('-inf')
while l <= r:
    re = max(re,inp[l][1]+inp[r][1])
    if inp[l][0]>1:
        inp[l][0]-=1
    else:
        l+=1
    if inp[r][0]>1:
        inp[r][0]-=1
    else:
        r-=1
print(re)