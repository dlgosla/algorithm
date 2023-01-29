from collections import defaultdict, deque

n, m = map(int, input().split())

edges = defaultdict(list)
visited = defaultdict(lambda: False)
for i in range(m):
    a, b = map(int, input().split())
    edges[a].append(b)
    edges[b].append(a)

count = 0
for i in range(1, n + 1):
    if i in visited:
        continue

    dq = deque([i])
    visited[i] = True
    while dq:
        node = dq.popleft()
        adjacent_nodes = edges[node]
        for adjacent_node in adjacent_nodes:
            if adjacent_node not in visited:
                visited[adjacent_node] = True
                dq.append(adjacent_node)

    count += 1

print(count)
