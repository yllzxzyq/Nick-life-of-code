def quicksort(i, j, nums,k):
    p = i
    l = i + 1
    r = j
    while r > l:
        while r > l and nums[r] > nums[p]:
            r -= 1
        if nums[r] < nums[p]:
            nums[r], nums[p] = nums[p], nums[r]
        p = r
        while r > l and nums[l] < nums[p]:
            l += 1
        nums[l], nums[p] = nums[p], nums[l]
        p = l
    if len(nums) - 1 - r > k:
        quicksort(r + 1, j, nums,k)
    elif len(nums) - 1 - r < k:
        quicksort(i, l - 1, nums,k)
    else:
        return r
nums = [6,3,2,5,8,5,4,7,9]
re = quicksort(0,len(nums)-1,nums,2)
print(re)