"""
행렬에서 최소 거리 
-> bfs 

2차원 배열로 visited 할 경우 아래 예시에서 답을 못구함

0101
0101
0001
1110

=> 벽을 부수고 간 경우 따로 벽을 안부수고 간 경우 따로 visited

"""

from collections import deque

n, m = map(int, input().split())

map = []
for i in range(n):
    map.append([int(i) for i in list(input())])


def bfs():
    visited = [[[False] * 2 for _ in range(m)] for _ in range(n)]
    visited[0][0][0] = True

    delta_r = [0, -1, 0, 1]
    delta_c = [1, 0, -1, 0]

    dq = deque([(0, 0, 0, map[0][0])])

    while dq:
        cr, cc, wall_broken, cost = dq.popleft()

        if (cr, cc) == (n - 1, m - 1):
            return cost + 1

        for dr, dc in zip(delta_r, delta_c):
            nr = cr + dr
            nc = cc + dc

            if 0 <= nr < n and 0 <= nc < m:
                new_wall_broken = wall_broken
                # 지금 가려는 곳에 벽이 있으면
                if map[nr][nc] == 1:
                    # 이전에 이미 벽을 부쉈으면 못부숨
                    if wall_broken:
                        continue
                    # 처음 벽을 만난 거면 벽 부수고 이동
                    else:
                        new_wall_broken = 1
                if not visited[nr][nc][new_wall_broken]:
                    visited[nr][nc][new_wall_broken] = True
                    dq.append((nr, nc, new_wall_broken, cost + 1))

    return -1


print(bfs())
