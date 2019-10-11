#暴力递归求最短路径,leetcode超限
def minPathSum1(grid) :
    m=len(grid)
    n=len(grid[0])
    x,y=0,0
    s=0
    re=[]
    def shortpath(x,y,s,L):
        s+=1
        L+=grid[y][x]
        if s==m+n-1:
            return re.append(L)
        if x<n-1:
            shortpath(x+1,y,s,L)
        if y<m-1:
            shortpath(x,y+1,s,L)
    shortpath(x,y,s,0)
    return min(re)
#二维动态规划方法
def minPathSum2(grid):
    m=len(grid)
    n=len(grid[0])
    R=[[0]*n for i in range(m)]
    R[0][0]=grid[0][0]
    for j in range(1,n):
        R[0][j]=grid[0][j]+R[0][j-1]
    for i in range(1,m):
        for j in range(n):
            if j==0:
                R[i][j]=R[i-1][j]+grid[i][j]
            else:
                R[i][j]=min(R[i-1][j],R[i][j-1])+grid[i][j]
    return R[m-1][n-1]

#原数组进行修改，空间复杂度O(1)
def minPathSum3(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if i==0 and j!=0:
                grid[i][j] = grid[i][j-1] + grid[i][j]
            elif j==0 and i!=0:
                grid[i][j] = grid[i-1][j]+grid[i][j]
            elif j!=0 and i!=0:
                grid[i][j] = min(grid[i-1][j],grid[i][j-1])+grid[i][j]
    return grid[-1][-1]


grid=[
  [1,3,12,1],
  [1,5,1,3],
  [4,2,1,4]
]
R=minPathSum3(grid)
print(R)

