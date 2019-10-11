nums = list(map(int,input().split(',')))
def J(nums):
    if len(nums)<=1:
        return 1
    l = 0
    r = nums[l]
    while r<len(nums) and l!=r:
        max_r = 0
        for i in range(l+1,r+1):
            max_r = max(nums[i]+i,max_r)
        l = r
        r = max_r
    if r>=len(nums):
        return 1
    else:
        return 0
print(J(nums))