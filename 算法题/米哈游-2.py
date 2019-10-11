R,C = map(int,input().split())
L = [[0]*C for i in range(R)]
for i in range(R):
    line = input()
    for j in range(len(line)):
        L[i][j] = line[j]
last = list(map(int,input().split()))
x1 = last[:2]
x2 = last[2:]
L[x1[0]][x1[1]],L[x2[0]][x2[1]] = L[x2[0]][x2[1]],L[x1[0]][x1[1]]
def change(L,sums):
    point_j =[]
    for i in range(R):
        j = 2
        stack = []
        while j < C:
            if L[i][j] !=0 and L[i][j-2] == L[i][j] and L[i][j-1] == L[i][j]:
                point_j.append([i,j])
                stack = [j-2,j-1]
                j += 1
                while j < C and L[i][j] == L[i][j-1]:
                    stack.append(j)
                    j+=1
            j += 1
        sums += len(stack)
        for i1 in range(i-1,0,-1):
            for j1 in range(len(stack)):
                L[i1][j1] = L[i1-1][j1]
        for j1 in range(len(stack)):
            L[0][j1] = 0
    print(L)
    for j in range(C):
        i = 2
        stack_i = []
        while i < R:
            if L[i][j] !=0 and L[i-2][j] == L[i][j] and L[i-1][j] == L[i][j]:
                stack_i = [i-2,i-1]
                while i < R and L[i][j] == L[i-1][j]:
                    stack_i.append(i)
                    i+=1
            i += 1
        sums += len(stack_i)
        for i1 in range(len(stack_i)):
            if i1 >= len(stack_i):
                L[i1][j] = L[i1-len(stack_i)][j]
        for i1 in range(len(stack_i)):
            L[i1][j] = 0
    print(L)
    return sums

re = 0
print(change(L,re))
