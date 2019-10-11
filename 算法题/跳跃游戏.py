def X():
    nums=[1,2,3]
    if len(nums) == 1:
        return True
    l = 0
    m = nums[l]
    while m < len(nums) - 1:
        M = m
        for i in range(l, m+1):
            if i + nums[i] > m:
                m = i + nums[i]
            if m >= len(nums) - 1:
                return True
        if l == m and m < len(nums) - 1:
            return False
        l = M
    return True
t = X()
print(t)