from collections import deque

from collections import deque


def solution():
    r, c = map(int, input().split())

    roads = [[0 for j in range(c)] for i in range(r)]
    dq = deque()
    # water_dq = deque()
    water = []
    visited = []
    for i in range(r):
        for j, elem in enumerate(input()):
            if elem == "S":
                dq.append((i, j, 0))
                visited.append((i, j))
            elif elem == "*":
                water.append((i, j))

            roads[i][j] = elem

    dr = [0, 1, -1, 0]
    dc = [-1, 0, 0, 1]
    # print(roads)

    while dq:
        temp = []
        for (i, j) in water:
            for _dr, _dc in zip(dr, dc):
                nr = i + _dr
                nc = j + _dc

                if 0 <= nr < r and 0 <= nc < c:
                    if roads[nr][nc] == ".":
                        roads[nr][nc] = "*"
                        temp.append((nr, nc))
        water = temp[:]
        print(roads)
        print(dq)

        i, j, count = dq.popleft()

        if roads[i][j] == "D":
            return count

        for _dr, _dc in zip(dr, dc):
            nr = i + _dr
            nc = j + _dc

            if 0 <= nr < r and 0 <= nc < c:
                if roads[nr][nc] in [".", "D"] and (nr, nc) not in visited:
                    visited.append((nr, nc))
                    dq.append((nr, nc, count + 1))

    return "KAKTUS"


print(solution())

"""
n초후에 가라앉는 땅

5 5
.....
..XXD
...XX
S....
....*

8 7 8 9 10
7 6 X X D 
6 5 4 X X 
5 4 3 2 1 
4 3 2 1 0

3 3
D.*
...
..S

D 1 0
4 2 1
4 3 2
"""
