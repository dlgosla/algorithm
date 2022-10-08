from collections import defaultdict, deque

n, m = map(int, input().split())

members = defaultdict(list)

for i in range(m):
    p1, p2 = map(int, input().split())

    members[p1].append(p2)
    members[p2].append(p1)


counts = defaultdict(int)

for i in range(1, n):
    for j in range(i + 1, n + 1):

        dq = deque([(i, 0)])
        visited = []

        while dq:
            node, count = dq.popleft()

            if node == j:
                break

            for m in members[node]:
                if m not in visited:
                    dq.append((m, count + 1))

        counts[i] += count
        counts[j] += count

counts = sorted(counts.items(), key=lambda x: (x[1], x[0]))

print(counts[0][0])
