import sys

input = sys.stdin.readline


class Stack:
    def __init__(self):
        self.lst = [-1] * 10000
        self.top_point = -1

    def push(self, elem):
        self.top_point += 1
        self.lst[self.top_point] = elem

    def pop(self):
        if self.top_point == -1:
            return -1

        elem = self.lst[self.top_point]
        # self.lst[self.top_point] = -1
        self.top_point -= 1

        return elem

    def empty(self):
        if self.top_point == -1:
            return 1
        else:
            return 0

    def top(self):
        if self.top_point == -1:
            return -1
        else:
            return self.lst[self.top_point]

    def size(self):
        return self.top_point + 1


stack = Stack()

n = int(input())

for i in range(n):
    operation = input().strip()

    if operation == "top":
        print(stack.top())
    elif operation == "empty":
        print(stack.empty())
    elif operation == "pop":

        print(stack.pop())
    elif operation == "size":
        print(stack.size())
    elif "push" in operation:
        elem = operation.split()[1]
        stack.push(elem)
