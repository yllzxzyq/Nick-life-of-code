def longestConsecutive(nums) :
    if not nums:
        return 0
    d = {}
    for i, v in enumerate(nums):
        if v not in d:
            d[v] = [v, v]
            if v - 1 in d:
                d[v] = [d[v - 1][0], d[v][1]]
                for j in range(d[v - 1][0],d[v][1]):
                    d[j] = [d[v][0], d[v][1]]
            if v + 1 in d:
                d[v] = [d[v][0], d[v + 1][1]]
                for j in range(d[v][0], d[v][1]+1):
                    d[j] = [d[v][0], d[v][1]]
    re = [x[1] - x[0] for x in d.values()]
    return max(re) + 1
print(longestConsecutive([0,3,7,2,5,8,4,6,0,1]))