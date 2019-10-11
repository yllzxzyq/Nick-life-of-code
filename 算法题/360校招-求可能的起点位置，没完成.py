import random


def GenerateRandomArray(size,start, end): # 产生一个随机数列长度为size，数字范围为-value~value
    array =[]
    for i in range(size):
        array.append(random.randint(start,end))
        #array.append((end-start)*random.random() + start)
    return array

n,m = 10,3
L=[5,2,6]

def helper(n,L,i,s):
    if s>=n or s<0:
        return False
    if i == len(L):
        if s<=n and s>=0:
            return True
        else:
            return False
    return helper(n,L,i+1,s+L[i]) or helper(n, L, i + 1, s-L[i])

re=0
for j in range(n):
    if helper(n,L,0,j):
        re+=1
print(re)