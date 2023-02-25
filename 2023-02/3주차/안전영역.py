"""
100x100x100 = 1,000,000 -> 완탐

1~영역에서 가장 큰 수까지 높이로 설정하고
해당 높이에서 잠기지 않은 영역의 수를 세면 됨
-> bfs or dfs로 잠기지 않은 영역들을 탐색하고 그 영역 개수를 세면 됨

"""

from collections import deque

n = int(input())
area = [[] for i in range(n)]
max_num = 0
for i in range(n):
    for elem in input().split():
        elem = int(elem)
        max_num = max(max_num, elem)
        area[i].append(elem)

dr = [0, 1, -1, 0]
dc = [1, 0, 0, -1]


max_count = 1
for k in range(1, max_num + 1):
    visited = [[False] * n for _ in range(n)]
    curr_count = 0

    for i in range(n):
        for j in range(n):
            if visited[i][j] or area[i][j] <= k:
                continue

            curr_count += 1

            dq = deque([(i, j)])
            visited[i][j] = True

            while dq:
                cr, cc = dq.popleft()

                for _dr, _dc in zip(dr, dc):
                    nr = cr + _dr
                    nc = cc + _dc

                    if 0 <= nr < n and 0 <= nc < n:
                        if not visited[nr][nc] and area[nr][nc] > k:
                            dq.append((nr, nc))
                            visited[nr][nc] = True

    max_count = max(curr_count, max_count)
print(max_count)
