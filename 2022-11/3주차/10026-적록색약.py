"""
정신놓고 다른 변수에다가 계산하진 않았는 지 확인하기
n이 100정도면 두번 완탐해도 괜찮다 괜히 어렵게 생각하지 말자
구역 개수 찾을 때는 visited로! 완탐으로!
"""

from collections import deque

n = int(input())

colors = []
for i in range(n):
    colors.append(input())

# n = 100
# colors = ["R" * n for i in range(n)]

normal_visited = [[False] * n for i in range(n)]
delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]

normal_count = 0
blue_count = 0
rg_count = 0
# blind_count = 0
# blind_dq = deque()


for i in range(n):
    for j in range(n):
        if normal_visited[i][j]:
            continue

        normal_visited[i][j] = True
        normal_dq = deque([(i, j)])
        curr_color = colors[i][j]

        while normal_dq:
            cr, cc = normal_dq.pop()

            for dr, dc in delta:
                nr = cr + dr
                nc = cc + dc

                if not (0 <= nr < n and 0 <= nc < n):
                    continue
                if normal_visited[nr][nc]:
                    continue

                if curr_color == colors[nr][nc]:
                    normal_dq.append((nr, nc))
                    normal_visited[nr][nc] = True

        normal_count += 1
        if curr_color == "B":
            blue_count += 1

        # if curr_color == "R":
        #     blind_dq.append((i, j))

blind_visited = [[False] * n for i in range(n)]
for i in range(n):
    for j in range(n):
        if blind_visited[i][j]:
            continue

        curr_color = colors[i][j]
        if curr_color == "B":
            continue

        blind_visited[i][j] = True
        blind_dq = deque([(i, j)])

        while blind_dq:
            cr, cc = blind_dq.pop()

            for dr, dc in delta:
                nr = cr + dr
                nc = cc + dc

                if not (0 <= nr < n and 0 <= nc < n):
                    continue
                if blind_visited[nr][nc]:
                    continue

                if colors[nr][nc] == "R" or colors[nr][nc] == "G":
                    blind_dq.append((nr, nc))
                    blind_visited[nr][nc] = True

        rg_count += 1


print(normal_count, blue_count + rg_count)
