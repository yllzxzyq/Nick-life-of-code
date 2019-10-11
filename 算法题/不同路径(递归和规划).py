#递归算法，复杂度2^n
def D(i, j):
    if i == 1 or j == 1:
        return 1
    else:
        return D(i - 1, j) + D(i, j - 1)

#动态规划，复杂度m*n
def G(m,n):
    L = [[1] * m] * n
    for i in range(1,n):
        for j in range(1,m):
            L[i][j]=L[i][j-1]+L[i-1][j]
    return L[n-1][m-1]

print(G(7,3))