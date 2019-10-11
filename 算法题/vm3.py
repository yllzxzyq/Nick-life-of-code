a,b,k = map(int,input().split())
re = 0
target = True

if target:
    for i in range(a,b+1):
        if i%k ==0:
            if k<=2:
                re+=1
            else:
                if i//k>=k:
                    re+=1
print(re)
