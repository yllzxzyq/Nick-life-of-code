n,m = map(int,input().split(' '))
tests= list(map(int,input().split(' ')))

R=[]
for i in range(tests[-1]+1):
    if i not in tests:
        R.append(i)
R.append(tests[-1]+1)
L=[]
for i in range(m):
    L.append(int(input()))
for i in range(m):
    if L[i]>R[-1]:
        print(L[i])
    else:
        j=0
        while L[i] > R[j]:
            j+=1
        print(R[j])
# 5 6
# 1 2 3 5 6
# 3
# 2
# 1
# 4
# 5
# 6