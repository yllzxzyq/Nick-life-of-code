m,n = map(int, input().split(' '))
works=[]
for i in range(m):
    works.append(list(map(int, input().split(' '))))
people=list(map(int, input().split(' ')))
def printM(works,a):
    mmax=0
    for i in works:
        if i[0]<=a:
            mmax=max(mmax,i[1])
    print(mmax)
for j in people:
    printM(works,j)
# 3 3
# 1 100
# 10 1000
# 1000000000 1001
# 9 10 1000000000
import sys
def main():
    lines = sys.stdin.readlines()
    lines = [l.strip().split() for l in lines if l.strip()]
    n, m = int(lines[0][0]), int(lines[0][1])
    res = [0] * (n + m)
    abilities = list(map(int, lines[-1]))
    maps = dict()
    for index, l in enumerate(lines[1:-1]):
        d, s = int(l[0]), int(l[1])
        maps[d] = s
        res[index] = d
    for index, ability in enumerate(abilities):
        res[index + n] = ability
        if ability not in maps:
            maps[ability] = 0
    res.sort()
    maxSalary = 0
    for index in range(n + m):
        maxSalary = max(maxSalary, maps[res[index]])
        maps[res[index]] = maxSalary
    for index in range(m):
        print(maps[abilities[index]])
if __name__ == '__main__':
    main()