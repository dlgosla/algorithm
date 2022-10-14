from collections import deque

n, m = map(int, input().split())

maze = []
for i in range(n):
    maze.append(list(input()))

delta = [(0, 1), (0, -1), (1, 0), (-1, 0)]

dq = deque([(0, 0, 0)])

visited = []
while dq:
    row, col, count = dq.popleft()
    # print(row, col)

    if row == n - 1 and col == m - 1:
        print(count + 1)
        break

    for dr, dc in delta:
        nr = row + dr
        nc = col + dc

        if not 0 <= nr < n or not 0 <= nc < m:
            continue

        if maze[nr][nc] == "1" and (nr, nc) not in visited:
            # print(nr, nc, maze[nr][nc])
            dq.append((nr, nc, count + 1))
            visited.append((nr, nc))
