# t = int(input())
def qier(n,s):
    if n <11:
        print('NO')
    else:
        for j in range(n):
            if s[j]=='8':
                break
        if n-j>=11:
            print('YES')
        else:
            print('NO')

# for i in range(t):
#     n = int(input())
#     s = input()
qier(11,'18888888888')
