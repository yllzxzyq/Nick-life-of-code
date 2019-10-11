n,k = map(int,input().split())
L = list(map(int,input().split()))
L.sort().reverse()
for i in range(k):
    if L:
        x=L.pop()
        print(x)
        for j in L:
            j-=x
    else:
        print(0)