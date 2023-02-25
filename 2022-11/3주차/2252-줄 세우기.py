from collections import deque, defaultdict

n, m = map(int, input().split())

graph = defaultdict(list)
indegree = [0] * (n + 1)
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

dq = deque()
answer = []
for i in range(1, n + 1):
    if indegree[i] == 0:
        dq.append(i)

while dq:
    student = dq.popleft()
    answer.append(student)

    for next_studnt in graph[student]:
        indegree[next_studnt] -= 1
        if indegree[next_studnt] == 0:
            dq.append(next_studnt)

print(*answer)
