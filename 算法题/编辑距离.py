word1 = ' '+'sdfafdsaf'
word2 = ' '+'djafkafk'
n=len(word1)+1
m=len(word2)+1
Re=[[0]*n for i in range(m)]
for i in range(m):
    for j in range(n):
        if i==0 and j!=0:
            Re[i][j]=1+Re[i][j-1]
        elif j==0 and i!=0:
            Re[i][j]=1+Re[i-1][j]
        elif i!=0 and j!=0:
            if word1[j-1]==word2[i-1]:
                Re[i][j]=Re[i-1][j-1]
            else:
                Re[i][j]=min(Re[i-1][j-1],Re[i-1][j],Re[i][j-1])+1
print(Re)



