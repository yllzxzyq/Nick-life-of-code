def leap_insert(nums,index):
    while(nums[index]>nums[(index-1)//2]):
        if index == 0:
            return
        nums[index], nums[(index-1)//2] = nums[(index-1)//2], nums[index]
        index=(index-1)//2



def adjust(nums,r):
    x=0
    while 2*x+1<len(nums)-r:
        if nums[x]<nums[2*x+1]:
            if 2*x+2<len(nums)-r and nums[2*x+1]<nums[2*x+2]:
                nums[x], nums[2*x+2] = nums[2*x+2], nums[x]
                x=2*x+2
            else:
                nums[x], nums[2 * x + 1] = nums[2 * x + 1], nums[x]
                x = 2 * x + 1
        else:
            return

L=[45,6,7,8,1,2,3]
for i in range(1,len(L)):
    leap_insert(L,i)
for r in range(1,len(L)):
    L[0], L[-r] = L[-r], L[0]
    adjust(L,r)
print(L)




