#求和为target的不降序无重复二元组，按升序排列
n, k =map(int,input().split())
nums = list(map(int,input().split()))
l,r = 0,n-1
re = []
x = float('inf')
while r > l:
    if nums[l]+nums[r]<k:
        l+=1
    elif nums[l]+nums[r]>k:
        r-=1
    else:
        if nums[l] !=x :
            print(str(nums[l])+' '+str(nums[r]))
        x = nums[l]
        l+=1
        r-=1
# 10 10
# -8 -4 -3 0 1 2 4 5 8 9

#补充版，求和为target的不降序无重复三元组，按升序排列
n, k =map(int,input().split())
nums = list(map(int,input().split()))
def search(i,nums,target):
    l,r = i+1,n-1
    x = float('inf')
    while r > l:
        if nums[l]+nums[r] < target:
            l+=1
        elif nums[l]+nums[r] > target:
            r-=1
        else:
            if nums[l] !=x:
                print(str(nums[i])+' '+str(nums[l])+' '+str(nums[r]))
            x = nums[l]
            l+=1
            r-=1
    return
y = float('inf')
for j in range(len(nums)-2):
    if nums[j] != y:
        search(j,nums,k-nums[j])
        y = nums[j]