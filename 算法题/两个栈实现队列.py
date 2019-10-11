class stack:
    def __init__(self):
        self.l = []

    def pop(self):
        return self.l.pop()

    def peek(self):
        return self.l[-1]

    def push(self, v):
        self.l.append(v)

    def is_empty(self):
        return not self.l

    def lenght(self):
        return len(self.l)


stack1 = stack()
stack2 = stack()
n = int(input())
for j in range(n):
    line = input().split()
    if len(line) == 2:
        stack1.push(int(line[1]))
    elif line[0] == 'peek':#代码注意数据类型，忘记切片影响很大
        if stack2.is_empty():
            for i in range(stack1.lenght()):
                stack2.push(stack1.pop())
        print(stack2.peek())
    else:
        if stack2.is_empty():
            for i in range(stack1.lenght()):
                stack2.push(stack1.pop())
        stack2.pop()