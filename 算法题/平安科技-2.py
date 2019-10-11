inp = input().split()
s = inp[0]
p = inp[1]
S = set(s)
P = set(p)
if S==P:
    print('true')
else:
    print('false')