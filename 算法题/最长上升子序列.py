class Solution:
    def lengthOfLIS(self, nums) -> int:
        if not nums:
            return 0
        L = []
        cur = []
        def son_nums(nums,cur,L, i):
            if i == len(nums):
                L.append(cur)
                return
            son_nums(nums,cur+[nums[i]],L,i+1)
            son_nums(nums,cur,L,i+1)
        son_nums(nums,cur,L,0)
        print(L)
        re = 0
        for i in L:
            l = 1
            for j in range(len(i)-1):
                if i[j+1]-i[j]>0:
                    l+=1
                else:
                    l=0
            re = max(re,l)
        return re
s = Solution()
nums = [-2,-1]
print(s.lengthOfLIS(nums))