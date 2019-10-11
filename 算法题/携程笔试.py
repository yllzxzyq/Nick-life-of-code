s = 'aabbcddcabab'
d = {}
lens = 0
R = []
for r in range(len(s)):
    if s[r] not in d :
        d[s[r]] = 1
    else:
        d[s[r]] = 0
        lens+=2
    if 1 not in d.values():
        R.append(lens)
        lens = 0

re=''
for i in R:
    re += str(i)+','
print(re[:-1])