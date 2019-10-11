import random
# arr=[1,2,3,4,5,9,10]
# k,x=5,6
# l,r=0,0
def GenerateRandomArray(size,start, end): # 产生一个随机数列长度为size，数字范围为-value~value
    array =[]
    for i in range(size):
        array.append(random.randint(start,end))
        #array.append((end-start)*random.random() + start)
    return array
# arr=GenerateRandomArray(10,1,100)
# arr.sort()
# k=5
# x=50
# arr=list(map(int,input().split(',')))
# # k=int(input())
# # x=int(input())
arr=list(map(int,input().split(',')))
k=int(input())
x=int(input())
re=''
for i in range(len(arr)):
    if arr[i]>x:
        r=i
        break
if r==0:
    for x in arr[:k+1]:
        re=re+str(x)+','
else:
    l=r-1
    while r-l+1<k:
        if l>0 and r<len(arr)-1:
            if arr[r]-x>=x-arr[l]:
                l-=1
            else:
                r+=1
        elif r==len(arr)-1:
            l-=1
        elif l==0:
            r+=1
    for x in arr[l:r+1]:
        re=re+str(x)+','
print(re[:-1])
