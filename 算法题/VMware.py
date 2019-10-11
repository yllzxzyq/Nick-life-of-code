T = int(input())
inp = []
for i in range(T):
    inp.append(list(map(int,input().split())))
print(inp)
def pri(v):
    if v[0]%2 == 0 :
        re = ''
        s = str(v[1]-1)
        for j in range(1,v[0]//2+1):
            if j < len(s):
                re = s[-j] + re
                re = re + s[-j]
            elif j == len(s):
                if j < v[0]//2:
                    re = s[-j] + re
                    re = re + s[-j]
                else:
                    re = str(int(s[-j]) + 1) + re
                    re = re + str(int(s[-j]) + 1)
            else:
                if j < v[0]//2:
                    re = '0' + re
                    re = re + '0'
                else:
                    re = '1' + re
                    re = re + '1'

    else:
        re = ''
        s = str(v[1] - 1)
        for j in range(1, v[0] // 2 + 2):
            if j == 1:
                re = s[-j]
            elif j < len(s):
                re = s[-j] + re
                re = re + s[-j]
            elif j == len(s):
                if j < v[0] // 2+1:
                    re = s[-j] + re
                    re = re + s[-j]
                else:
                    re = str(int(s[-j]) + 1) + re
                    re = re + str(int(s[-j]) + 1)
            else:
                if j < v[0] // 2+1:
                    re = '0' + re
                    re = re + '0'
                else:
                    re = '1' + re
                    re = re + '1'
    print(re)

for v in inp:
    pri(v)