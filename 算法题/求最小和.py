def minSubArray2(nums,m) :
    if m>len(nums):
        return
    re = float('inf')
    for i in range(len(nums)):
        sum1 = 0
        for j in range(i,len(nums)):
            sum1+=nums[j]
            if j-i>=m-1:
                re = min(re,sum1)
    return re
def minSubArray(nums,m) :
    if m>len(nums):
        return
    re = float('inf')
    su = 0
    tag = 0
    for i in range(len(nums)):
        su += nums[i]
        tag+=1
        if su > 0:
            su = 0
            tag = 0
        if tag >= m:
            re = min(re,su)
    return re
n,m = map(int,input().split())
nums = list(map(int,input().split()))
R = minSubArray(nums,m)
print(R)
