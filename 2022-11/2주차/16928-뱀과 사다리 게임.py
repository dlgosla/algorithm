from collections import defaultdict, deque

n, m = map(int, input().split())

boards = [-1 for _ in range(101)]
for _ in range(n):
    x, y = map(int, input().split())
    boards[x] = y

for _ in range(m):
    u, v = map(int, input().split())
    boards[u] = v

dq = deque([(1, 0)])
visited = defaultdict(lambda: False)


def bfs():
    while dq:
        # print(dq)
        curr_idx, count = dq.popleft()

        for i in range(1, 7):
            next_idx = curr_idx + i
            if next_idx <= 100:
                next_number = boards[next_idx]
                if next_idx == 100:
                    return count + 1

                if next_number != -1:
                    dq.append((next_number, count + 1))
                    visited[next_number] = True

                else:
                    next_number = curr_idx + i
                    if not visited[next_number]:
                        dq.append((next_number, count + 1))
                        visited[next_number] = True


print(bfs())
