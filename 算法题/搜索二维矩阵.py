class Solution(object):
    #暴力法，遍历整个二维数组,复杂度O(N*M)
    def searchMatrix_1(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        for i in matrix:
            for j in i:
                if j ==target:
                    return True
        return False
    #动态规划,复杂度O(n+m)
    def searchMatrix_2(self, matrix, target):
        n = len(matrix)
        m = len(matrix[0])
        if not matrix or not matrix[0]:
            return False
        i,j = n-1,0
        while i >= 0 and j<m:
            if matrix[i][j] > target:
                i -= 1
            elif matrix[i][j] < target:
                j += 1
            else:
                return True
        return  False
    #方法三，二分查找
matrix = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
target = 9
s = Solution()
print(s.searchMatrix_2(matrix,target))