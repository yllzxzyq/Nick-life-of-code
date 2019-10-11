str1,str2,s = input().split()
def zuhe(str1,str2,s):
    n =len(s)
    point1 = len(str1)-1
    point2 = len(str2)-1
    for i in range(n-1,-1,-1):
        if s[i] == str1[point1]:
            point1-=1
        elif s[i] == str2[point2]:
            point2-=1
        else:
            return 0
    return 1
print(zuhe(str1,str2,s))
