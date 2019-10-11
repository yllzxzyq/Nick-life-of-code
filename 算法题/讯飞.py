'''
第一题，一只蜗牛在竹竿上，蜗牛第一天掉落一半再掉3米，第
二天掉落一半再掉3米，第三天掉落一半再掉6米，第四天掉落
一半再掉9米，第五天掉落一半再掉15米，依次类推...
输入一共掉落的天数，输出竹子的长度
'''
n = int(input())
start = 0
L = [3,3]
for i in range(2,n):
    L.append(L[i-2]+L[i-1])
for i in range(n-1,-1,-1):
    start += L[i]
    start = 2*start
print(start)

#第二题，求多段字符串中纯英文子串的首尾ASCII码值之差的绝对值之和
def is_word(i):
    if ord(i) >=65 and ord(i)<=90:
        return ord(i)
    elif ord(i) >= 97 and ord(i)<=122:
        return ord(i)
    else:
        return 0

def sum_words(s):
    if len(s) < 2:
        return 0
    for i in s:
        if not is_word(i):
            return 0
    return abs(ord(s[0])-ord(s[-1]))

L = input().split(';')
re = 0
for s in L:
    re += sum_words(s)
print(re)