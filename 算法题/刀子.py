L = []
n = 100000
for i in range(n):
    L.append(i+1)
index = 0
target = 1
while len(L)>1:
    if index == len(L):
        index =0
    if target % 3 ==0:
        L.pop(index)
        index-=1
    index+=1
    target+=1
print(L[0])

