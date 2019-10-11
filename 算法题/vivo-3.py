def solution(L):
    n= len(L)
    su = sum(L)
    re = [0]*(n//2+1)
    for i in range(1,n+1):
        for j in range(n//2,0,-1):
            if j >= 1:
                if abs(su-re[j]-re[j]) < abs(su-re[j-1]-L[i-1]-re[j-1]-L[i-1]):
                    re[j] = re[j]
                else:
                    re[j] = re[j-1]+L[i-1]
    return abs(re[-1]-su+re[-1])
stone_list = [3,7, 4, 11 ,8 ,10]
print(solution(stone_list))