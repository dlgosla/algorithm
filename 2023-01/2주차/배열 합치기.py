from collections import deque

n, m = map(int, input().split())
a = deque(list(map(int, input().split())))
b = deque(list(map(int, input().split())))

answer = []
while a and b:
    if a[0] > b[0]:
        answer.append(b.popleft())
    else:
        answer.append(a.popleft())

answer.extend(a)
answer.extend(b)

print(*answer)
