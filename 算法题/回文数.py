def isPalindrome(x) :
    import copy
    if x < 0 or (x % 10 == 0 and x != 0):
        return False
    x_copy = copy.deepcopy(x)
    x_reverse = 0
    while x > x_reverse:
        x_reverse = x_copy % 10 + x_reverse * 10
        x_copy = x_copy // 10
    return x == x_reverse
isPalindrome(121)