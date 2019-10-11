s = 'aabbcddc'
start = {}
end = {}
R = []
for index in range(len(s)):
    if s[index] not in start:
        start[s[index]] = index
for endin in range(len(s)-1,-1,-1):
    if s[endin] not in end:
        end[s[endin]] = endin

for x in start.keys():
    R.append([start[x],end[x]])

R.sort(key= lambda x : x[0])


def merge(intervals):
    n = len(intervals)
    if n == 0:
        return []
    intervals.sort(key=lambda x: x[0])
    l = [intervals[0]]
    for i in range(1, n):
        if l[-1][1] >= intervals[i][0]:
            l[-1][1] = max(l[-1][1], intervals[i][-1])
        else:
            l.append(intervals[i])
    return l

R=merge(R)

re=''
for i in R:
    re += str(i[1]-i[0]+1)+','
print(re[:-1])