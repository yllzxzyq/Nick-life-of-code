class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.mins = []
        self.index = -1

    def push(self, x: int) -> None:
        self.index += 1
        self.stack.append(x)
        if not self.mins:
            self.mins.append([x, self.index])
        else:
            if x < self.mins[-1][0]:
                self.mins.append([x, self.index])

    def pop(self) -> None:
        self.index -= 1
        x = self.stack.pop()
        if self.mins:
            if self.index < self.mins[-1][1]:
                self.mins.pop()
        return

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        if self.mins:
            return self.mins[-1][0]
        else:
            return

obj = MinStack()
obj.push(1)
obj.push(2)
obj.pop()
param_3 = obj.top()
param_4 = obj.getMin()
print(param_3)
print(param_4)
print(obj.stack)
print(obj.mins)

n = int(input())
mins = MinStack()
for i in range(n):
    line = input().split()
    if len(line)==2:
        mins.push(int(line[1]))
    elif line[0] == 'pop':
        mins.pop()
    else:
        print(mins.getMin())