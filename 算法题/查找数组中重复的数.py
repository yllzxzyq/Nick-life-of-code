nums = [1,2,3,5,6,4,1,1]
# len(nums)>max(nums)

for i in range(len(nums)):
    current = nums[i]
    for j in range(i+1,len(nums)):
        if current == nums[j]:
            break
print(current)