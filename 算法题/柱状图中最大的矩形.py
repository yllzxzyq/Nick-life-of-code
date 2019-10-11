#方案一，暴力法一，以每个高度求一次面积
def largestRectangleArea( heights):
    Re = 0
    def area(h, heights):
        re = 0
        s = 0
        for i in range(len(heights)):
            if heights[i] >= h:
                s += h
                re = max(s, re)
            else:
                s = 0
        return re

    for i in heights:
        Re = max(Re, area(i, heights))
    return Re
#方案二，暴力法二，求每俩个柱子中间的面积
def largestRectangleArea2(heights):
    Re = 0
    for i in range(len(heights)):
        minh=heights[i]
        s=heights[i]
        for j in range(i,len(heights)):
            minh=min(minh,heights[j])
            s=max(s,minh*(j-i+1))
        Re=max(Re,s)
    return Re
#方案三，单调栈（自己写的）
def largestRectangleArea3(heights):
    if len(heights) == 0:
        return 0
    L = [[heights[0], 1]]
    Re = heights[0]
    for i in range(1, len(heights)):
        if heights[i] >= L[-1][0]:
            L.append([heights[i], 1])
        else:
            while L and L[-1][0] >= heights[i]:
                last=L.pop()
                Re = max(Re, last[0] * last[1])
                if L and L[-1][0] >= heights[i]:
                    L[-1][1]+=last[1]
            L.append([heights[i], last[1]+1])
    while L:
        last = L.pop()
        Re = max(Re, last[0] * last[1])
        if L:
            L[-1][1] += last[1]
    return Re
#方案四，单调栈（模板）
def largestRectangleArea4(heights):
    stack = []
    result = 0
    heights.append(0)
    for i in range(len(heights)):
        top = i
        while stack != [] and heights[i] < heights[stack[-1]]:
            top = stack.pop()
            result = max((i-top)*heights[top], result)
        if stack == [] or heights[i] > heights[stack[-1]]:
            heights[top] = heights[i]
            stack.append(top)
    return result
heights=[2,1,4,5,1,3,3]
print(largestRectangleArea4(heights))


