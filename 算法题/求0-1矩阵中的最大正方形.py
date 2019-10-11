#暴力法，O（n^3)
def maximalSquare(matrix):
    def search1(lx, ly, n, matrix):
        t = True
        for i in range(n + 1):
            if matrix[ly + n][lx + i] != '1':
                t = False
        for i in range(n + 1):
            if matrix[ly + i][lx + n] != '1':
                t = False
        return t

    Re = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == '1':
                Re = max(Re, 1)
                t = 1
                while i + t < len(matrix) and j + t < len(matrix[0]) and search1(j, i, t, matrix):
                    Re = max(Re, (t + 1) ** 2)
                    t += 1
    return Re
# 动态规划
def maximalSquare1(matrix):
    Re=0
    dp=[[0]*len(matrix[0]) for i in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j]=='1':
                if i==0:
                    dp[i][j]=int(matrix[i][j])
                elif j==0:
                    dp[i][j]=int(matrix[i][j])
                else:
                    dp[i][j]=min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])+int(matrix[i][j])
            Re=max(Re,dp[i][j])
    return Re**2


matrix=[["1","0","1","1","0","1"],
 ["1","1","1","1","1","1"],
 ["0","1","1","0","1","1"],
 ["1","1","1","0","1","0"],
 ["0","1","1","1","1","1"],
 ["1","1","0","1","1","1"]]

print(maximalSquare1(matrix))