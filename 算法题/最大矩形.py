def maximalRectangle(matrix):
    Result = 0
    R = [0] * len(matrix[0])

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if int(matrix[i][j]) == 0:
                R[j] = 0
            else:
                R[j] = R[j] + int(matrix[i][j])
        Result = max(Result, area(R))
    return Result
def area(nums):
    re = 0
    L = [[-1, -1]]
    for i, v in enumerate(nums):
        if v > L[-1][0]:
            L.append([v, i])
        elif v < L[-1][0]:
            while v <= L[-1][0]:
                re = max(re, (i - L[-1][1]) * L[-1][0])
                x=L.pop()
            if v != L[-1]:
                L.append([v,x[1]])
    while len(L) > 1:
        re = max(re, (len(nums) - L[-1][1]) * L[-1][0])
        L.pop()
    return re
matrix = [["0","1"],["1","0"]]
print(maximalRectangle(matrix))