n = int(input())
T=[]
F=[]
for x in range(n):
    r=list(map(float,input().split()))
    if r[0]==1:
        T.append(r)
    else:
        F.append(r)

auc=0
for i in range(len(T)):
    for j in range(len(F)):
        if T[i][1]>F[j][1]:
            auc+=1
auc=auc/(len(T)*len(F))
print("{:.2f}".format(auc))