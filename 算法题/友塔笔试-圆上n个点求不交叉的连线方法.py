n=int(input())
if n>=4:
    R=[0]*(n//2+1)
R[0]=1
R[1]=1
if n%2==0:
    N=n//2
    for i in range(2,N+1):
        r=0
        for j in range(i):
            r += R[i-j-1]*R[j]
        R[i]=r
    print(R[N])
else:
    N=(n-1)//2
    for i in range(2, N + 1):
        r = 0
        for j in range(i):
            r += R[i - j - 1] * R[j]
        R[i]=r
    print(R[N]*n)
