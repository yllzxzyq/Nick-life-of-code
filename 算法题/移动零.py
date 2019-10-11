class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        from collections import deque
        n = len(nums)
        first_0 = deque()
        num = 0
        for i in range(n):
            if nums[i] == 0:
                num +=1
                first_0.append(i)
            else:
                if first_0:
                    nums[first_0.popleft()] = nums[i]
                    first_0.append(i)
        for i in range(n-num,n):
            nums[i] = 0
    def moveZeroes_1(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        index = 0
        for i in range(n):
            if nums[i] != 0:
                if i > index:
                    nums[index] = nums[i]
                    nums[i] = 0
                index += 1