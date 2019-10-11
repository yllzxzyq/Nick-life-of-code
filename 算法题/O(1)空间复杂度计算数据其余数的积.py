class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        re = [1]*n
        for i in range(1,n):
            re[i] = re[i-1]*nums[i-1]
        right = 1
        for i in range(n-1,-1,-1):
            re[i] = re[i]*right
            right*=nums[i]
        return re