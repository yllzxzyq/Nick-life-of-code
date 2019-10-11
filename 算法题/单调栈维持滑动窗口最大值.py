class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        from collections import deque
        if not nums or not k:
            return
        heap = deque()
        n = len(nums)
        for i in range(k):
            while heap and nums[i] > heap[-1][0]:
                heap.pop()
            heap.append([nums[i], i])
        re = [heap[0][0]]
        for i in range(k, n):
            if i - k  >= heap[0][1]:
                heap.popleft()
            while heap and nums[i] > heap[-1][0]:
                heap.pop()
            heap.append([nums[i], i])
            re.append(heap[0][0])
        return re

nums = [1,3,-1,-3,5,3,6,7]
k = 3
s =Solution()
r = s.maxSlidingWindow(nums, k)
print(r)