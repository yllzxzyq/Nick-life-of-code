
def trans(S,L):
    for s in S:
        if L[s]=='0':
            L[s]='1'
        else:
            L[s]='0'
    return L

def helper(L,p,times):
    if '1' not in L or times>10:
        Re.append(times)
        return
    else:
        for j in range(8):
            if p==7:
                return helper(trans([0, 6, 7], L),j,times+1)
            else:
                return helper(trans([p - 1, p, p + 1], L),j,times+1)
L=['0', '0', '0', '0', '0', '0', '0', '0']
Re=[]
for i in range(8):
    helper(L,i,0)
print(Re.sort()[0])


