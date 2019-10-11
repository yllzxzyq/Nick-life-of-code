T = int(input())
inp = []
for i in range(T):
    inp.append(list(map(int,input().split())))

for v in inp:
    if v[0] % 2 == 0