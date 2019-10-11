def maxSubArray( nums) :
    re = nums[0]
    r = 0
    sum1 = 0
    while r < len(nums):
        sum1 += nums[r]
        if re < sum1:
            re = sum1
        if sum1 < 0:
            sum1 = 0
        r += 1
    return re
maxSubArray([-2,1,-3,4,-1,2,1,-5,4])