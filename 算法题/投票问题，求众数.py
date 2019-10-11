#求超过n/2的众数
def majorityElement(nums):
    l = 0
    su = 1
    while l < len(nums):
        r = l + 1
        while r < len(nums) and su > 0:
            if nums[r] == nums[l]:
                su += 1
            else:
                su -= 1
            r += 1
        if r >= len(nums):
            return nums[l]
        l = r
        su = 1
    return
#求超过n/3的众数
def majorityElement2(nums):
    R = []
    for i in nums:
        if str(i) not in R:
            if len(R) < 4:
                R.append(str(i))
                R.append(1)
            else:
                R[1] -= 1
                R[3] -= 1
                if R[3] == 0:
                    R = R[:2]
                if R[1] == 0:
                    R.pop(0)
                    R.pop(0)
        else:
            if str(i) == R[0]:
                R[1] += 1
            else:
                R[3] += 1
    for x in range(len(R) // 2):
        R[x * 2 + 1] = 0
    for i in nums:
        for j in range(len(R) // 2):
            if R[j * 2] == str(i):
                R[j * 2 + 1] += 1
    re = []
    for x in range(len(R) // 2):
        if R[x * 2 + 1] > len(nums) / 3:
            re.append(int(R[x * 2]))
    return re