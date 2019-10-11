n,m = map(int,input().split())
d = {}
for i in range(m):
    l = list(map(int,input().split()))
    if l[0] not in d:
        d[l[0]] = [l[1]]
    else:
        d[l[0]].append(l[1])
def search_circle(d):
    a = []
    for i in d.keys():





