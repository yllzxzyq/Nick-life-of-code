# s = input()
# inp = input().split()
# p = set(inp)
s = '中华民族从此站起来了'
p = ['中华', '民族', '中华民族','从此', '站起来了' ]
def splitword(s,p):
    re = []
    n = len(s)
    start = [0]
    for i in range(n):
        for j in rang
            e(len(start)-1,-1,-1):
            if s[start[j]:i+1] in p:
                start.append(i+1)
                while re and re[-1][0]>=start[j]:
                    re.pop()
                re.append([start[j],s[start[j]:i+1]])
                break
    return re
r = splitword(s,p)
re = ''
for i in r:
    re+=str(i[1])+'、'
print(re[:-1])

