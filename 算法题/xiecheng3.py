n = int(input())
m = int(input())
start = []
graph= [{} for i in range(n)]
for i in range(n):
    start.append(i)
for i in range(m):
    r= list(map(int,input().split()))
    graph[r[0]][r[1]] = r[2]


re = [0]*(n+1)
time = 0
R = []
best_p = [0]*(n+1)
def conflict(k):
  global n,graph,re,best_p,time
  if k < n and re[k] in re[:k]:
    return True
  if k == n and re[k] != re[0]:
    return True
  time1 = sum([graph[node1][node2] for node1,node2 in zip(re[:k], re[1:k+1])])
  if 0 < time < time1:
    return True
  return False
def helper(k):
  global n,a,b,c,d,e,graph,re,R,time,best_p
  if k > n:
    cost = sum([graph[node1][node2] for node1,node2 in zip(re[:-1], re[1:])])
    if time == 0 or cost < time:
      best_p = re[:]
      time = cost
  else:
    for node in graph[re[k-1]]:
      re[k] = node
      if not conflict(k):
        helper(k+1)
helper(0)
print(time)