def zuhe(L,n):
    su = sum(L)
    re = [0]*(n//2+1)
    for i in range(1,n+1):
        for j in range(n//2,0,-1):
            if j >= 1:
                if abs(su-re[j]-re[j]) < abs(su-re[j-1]-L[i-1]-re[j-1]-L[i-1]):
                    re[j] = re[j]
                else:
                    re[j] = re[j-1]+L[i-1]
    return re[-1],su-re[-1]

T = int(input())
for i in range(T):
    n = int(input())
    L = list(map(int,input().split()))
    re_1,re_2 = zuhe(L,n)
    if re_1>re_2:
        re_1,re_2 = re_2,re_1
    print(str(re_1)+' '+str(re_2))
