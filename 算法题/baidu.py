inp = list(map(int,input().split()))
a = inp[:4]
n = inp[4]
re = [0]*n
for i in range(n):
    if i <4:
        re[i] = a[i]
    else:
        re[i] = re[i-1]+re[i-3]+re[i-4]
print(re[-1]%(10**9+7))