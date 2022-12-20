from collections import deque


def solution():
    r, c = map(int, input().split())

    roads = [[0 for j in range(c)] for i in range(r)]
    dq = deque()

    water_dq = deque()
    visited = []
    for i in range(r):
        for j, elem in enumerate(input()):
            roads[i][j] = elem
            if elem == "S":
                dq.append((i, j, 0))
                visited.append((i, j))
            elif elem == "*":
                water_dq.append((i, j))
                roads[i][j] = 0

    dr = [0, 1, -1, 0]
    dc = [-1, 0, 0, 1]

    while water_dq:
        i, j = water_dq.popleft()
        sink_time = roads[i][j]

        for _dr, _dc in zip(dr, dc):
            nr = i + _dr
            nc = j + _dc

            if 0 <= nr < r and 0 <= nc < c:
                if roads[nr][nc] in [".", "S"]:
                    roads[nr][nc] = sink_time + 1
                    water_dq.append((nr, nc))

    while dq:
        i, j, count = dq.popleft()

        for _dr, _dc in zip(dr, dc):
            nr = i + _dr
            nc = j + _dc

            if 0 <= nr < r and 0 <= nc < c:
                if (nr, nc) not in visited:
                    if roads[nr][nc] == "D":
                        return count + 1

                    if roads[nr][nc] == "." or (
                        type(roads[nr][nc]) == int and roads[nr][nc] > count + 1
                    ):
                        visited.append((nr, nc))
                        dq.append((nr, nc, count + 1))

    return "KAKTUS"


print(solution())

"""
5 5
.....
..XXD
...XX
S....
....*

[[8, 7, 8, 9, 10], 
[7, 6, 'X', 'X', 'D'], 
[6, 5, 4, 'X', 'X'], 
[5(D), 4, 3, 2, 1], 
[4, 3, 2, 1, 0]]

"""
