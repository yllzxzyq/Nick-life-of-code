n = int(input())
L = list(map(int,input().split()))
def R(L):
    sum_0 = 0
    d = {}
    for i in range(n):
        if L[i] == 0:
            sum_0 += 1
    for i in L:
        if i != 0:
            if i not in d:
                d[i] = [i,i]
                if i-1 in d and i+1 in d:
                    d[i] = [d[i-1][0],d[i+1][1]]
                    d[i-1] = [d[i-1][0],d[i+1][1]]
                    d[i+1] = [d[i-1][0],d[i+1][1]]
                elif i+1 in d:
                    d[i] = [d[i][0],d[i+1][1]]
                    d[i+1] = [d[i][0],d[i+1][1]]
                elif i-1 in d:
                    d[i] = [d[i - 1][0], d[i][1]]
                    d[i - 1] = [d[i - 1][0], d[i][1]]
            else:
                return 'NO'+'+'+str(sum_0)
    print(d)

def r(L):
    L.sort()
    re = 'YES'
    sum_0 = 0
    for i in range(n):
        if L[i] == 0:
            sum_0 += 1
    cur = sum_0
    for i in range(n-1):
        if L[i] != 0:
            if L[i+1] - L[i] == 0:
                re = 'NO'
                break
            elif cur >= L[i + 1] - L[i]-1:
                cur -= L[i + 1] - L[i]-1
            else:
                re = 'NO'
                break
    print(re+'+'+str(sum_0))
r(L)