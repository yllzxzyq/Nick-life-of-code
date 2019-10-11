#简单递归
def climbStairs1(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return climbStairs1(n - 1) + climbStairs1(n - 2)

#动态规划，数组结构计算斐波那契数列
def climbStairs2(n):
    R = [1, 2]
    for i in range(2, n):
        R.append(R[i - 1] + R[i - 2])
    return R[n - 1]

#常量计算斐波那契数列
def climbStairs3(n):
    if n==1:
        return 1
    small=1
    big=2
    for i in range(2, n):
        big,small=small+big,big
    return big
print(climbStairs3(4))