L = [1,1,1]
def solution(step_list):
    l = len(step_list)
    if not step_list:
        return -1
    elif l==1:
        return 0
    else:
        cur = 0
        right = step_list[cur]
        times = 1
        while right < l-1 and cur != right:
            times+=1
            r = 0
            for i in range(cur+1, right+1):
                r = max(r, i + step_list[i])
            cur,right = right,r
        if right >= l-1:
            return times
        else:
            return -1
print(solution(L))



