n = int(input())
re = ''
if n > 0:
    while n >=1000:
        n -= 1000
        re += 'M'
    while n >= 500:
        n -= 500
        re += 'D'
    while n >= 100:
        n -= 100
        re += 'C'
    while n>=50:
        n -= 50
        re += 'L'
    while n>= 10:
        n -= 10
        re += 'X'
    while n>= 5:
        n -= 5
        re += 'V'
    while n>= 1:
        n -= 1
        re += 'I'
print(re)