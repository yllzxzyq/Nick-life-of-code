N,M = 6,3
def solution(N, M):
    L = []
    for i in range(1,N+1):
        L.append(i)
    cur = 0
    re = ''
    times = 1
    while L:
        times += 1
        cur += 1
        if cur > len(L)-1:
            cur -= len(L)
        if times%M == 0:
            re+= str(L[cur])+' '
            L.pop(cur)
            cur -=1
    return re
print(solution(N,M))

