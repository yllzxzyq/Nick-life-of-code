def quick_sort(i, j, nums):
    if i < j:
        p = nums[i]
        l = i
        r = j
        while r > l:
            while r>l and nums[r] >= p:
                r -= 1
            nums[l] = nums[r]
            while r>l and nums[l] <= p:
                l += 1
            nums[r] = nums[l]
        nums[l] = p
        quick_sort(i,l-1,nums)
        quick_sort(r+1,j,nums)
    return nums

nums = [6,3,2,5,8,5,4,7,9,100]
re = quick_sort(0,len(nums)-1,nums)
print(re)
