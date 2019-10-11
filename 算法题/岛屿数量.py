def numIslands( grid):
    sum1 = 0
    def kuosan(i, j, grid):
        if grid[i][j] == '1':
            grid[i][j] = '0'
        if i > 0 and grid[i - 1][j] == '1': kuosan(i - 1, j, grid)
        if i < len(grid) - 1 and grid[i + 1][j] == '1': kuosan(i + 1, j, grid)
        if j > 0 and grid[i][j - 1] == '1': kuosan(i, j - 1, grid)
        if j < len(grid[0]) - 1 and grid[i][j + 1] == '1': kuosan(i, j + 1, grid)

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                sum1 += 1
                kuosan(i, j, grid)
    return sum1

grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
print(numIslands(grid))