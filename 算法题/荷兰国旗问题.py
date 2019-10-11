def sortColors(nums) :
    if len(nums) <= 1:
        return
    l = 0
    mmin = 0
    mmax = len(nums) - 1
    while l < len(nums):
        if nums[l] < 1:
            nums[l], nums[mmin] = nums[mmin], nums[l]
            mmin += 1
            l += 1
        elif nums[l] > 1:
            nums[l], nums[mmax] = nums[mmax], nums[l]
            mmax -= 1
        else:
            l += 1
        if l == mmax + 1:
            break
r=[0,1,2,3,54,6,2,3,1,1,1]
sortColors(r)
print(r)