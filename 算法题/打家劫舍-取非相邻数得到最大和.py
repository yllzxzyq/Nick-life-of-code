def rob( nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    money1 = [0] * (len(nums) + 1)
    money0 = 0
    for i, v in enumerate(nums):
        money1[i + 1] = max(money0 + v, money1[i])
        money0 = money1[i]
    return money1[-1]

nums =[1,5,6,4,3,8,1,2]
print(rob(nums))