from collections import deque
from itertools import combinations
import copy

n, m = map(int, input().split())
# dq = deque()
matrix = [[0] * n for i in range(n)]
init = []
INF = float("inf")

for i in range(n):
    for j, elem in enumerate(input().split()):
        num = int(elem)
        matrix[i][j] = num

        matrix[i][j] = 0

        if num == 1:
            matrix[i][j] = "-"

        if num == 2:
            init.append((i, j))
            # dq.append((i, j))

dr = [1, 0, -1, 0]
dc = [0, -1, 0, 1]

sub_matrices = []
for (i, j) in init:
    dq = deque([(i, j)])
    sub_matrix = copy.deepcopy(matrix)
    while dq:
        r, c = dq.popleft()
        for (_dr, _dc) in zip(dr, dc):
            nr = r + _dr
            nc = c + _dc

            if (0 <= nr < n and 0 <= nc < n) and sub_matrix[nr][nc] == 0:
                sub_matrix[nr][nc] = sub_matrix[r][c] + 1
                dq.append((nr, nc))
    sub_matrices.append(sub_matrix)


answer = INF
for length in range(m, m + 1):
    combs = list(combinations(sub_matrices, length))

    for comb in combs:
        final_matrix = [[-1] * n for i in range(n)]

        for i in range(n):
            for j in range(n):
                if sub_matrix[i][j] != "-":
                    min_num = INF
                    for sub_matrix in comb:
                        if sub_matrix[i][j] != 0:
                            min_num = min(min_num, sub_matrix[i][j])
                    final_matrix[i][j] = min_num

        for (i, j) in init:
            final_matrix[i][j] = -1

        max_num = 0
        fail = False
        for i in range(n):
            for j in range(n):
                max_num = max(max_num, final_matrix[i][j])
                if final_matrix[i][j] == INF:
                    fail = True
                    break

        if not fail:
            answer = min(answer, max_num)

if answer != INF:
    print(answer)
else:
    print(-1)

# # dq = deque([(0, 0), (3, 0), (3, 6), (6, 4)])
# dq = deque([(0, 0), (1, 5), (4, 3)])
# temp = copy.deepcopy(matrix)
# while dq:
#     r, c = dq.popleft()

#     for (_dr, _dc) in zip(dr, dc):
#         nr = r + _dr
#         nc = c + _dc

#         if (0 <= nr < n and 0 <= nc < n) and temp[nr][nc] == 0:
#             dq.append((nr, nc))
#             temp[nr][nc] = temp[r][c] + 1

# print(temp)

# print(matrix)

# print(max(matrix))
"""
2 0 2 0 - - 0
0 0 - 0 - 2 0
0 - - 2 - 0 0
2 - 0 0 0 0 2
0 0 0 2 0 - -
0 - 0 0 0 0 0
2 - 0 0 2 0 2

2 0 2 0 - - 0
0 0 - 0 - 2 0
0 - - 2 - 0 0
2 - 0 1 0 0 2
0 0 1 2 1 - -
0 - 0 1 0 0 0
2 - 0 0 2 0 2

7 4
2 0 2 0 1 1 0
0 0 1 0 1 2 0
0 1 1 2 1 0 0
2 1 0 0 0 0 2
0 0 0 2 0 1 1
0 1 0 0 0 0 0
2 1 0 0 2 0 2

0 0 * 0 - - 0
0 0 - 0 - * 0
0 - - * - 0 0
! - 0 0 0 0 *
0 0 0 * 0 - -
0 - 0 0 0 0 0
! - 0 0 ! 0 *

0 0 * 0 - - 0
0 0 - 0 - * 0
1 - - * - 0 0
! - 0 0 0 0 *
1 0 0 * 0 - -
1 - 0 0 1 0 0
! - 0 1 ! 1 *

[0, 1, *, 3, -1, -1, 3], 
[1, 2, -1, 4, -1, *, 2], 
[1, -1, -1, *, -1, 2, 1], 
[0, -1, 4, 3, 2, 1, *], 
[1, 2, 3, *, 2, -1, -1], 
[2, -1, 3, 2, 1, 2, 3], 
[3, -1, 2, 1, 0, 1, *]]

[[2, 1, 2, 3, '-', '-', 3], 
[1, 2, '-', 4, '-', 3, 2], 
[1, '-', '-', 4, '-', 2, 1], 
[2, '-', 4, 3, 2, 1, 2], 
[1, 2, 3, 3, 2, '-', '-'], 
[2, '-', 3, 2, 1, 2, 3], 
[3, '-', 2, 1, 2, 1, 2]]

000
0 0 * 0 - - 0
0 0 - 0 - * 0
0 - - * - 0 0
! - 0 0 0 0 *
0 0 0 * 0 - -
0 - 0 0 0 0 0
! - 0 0 ! 0 *

[[2, 1, 2, 3, '-', '-', 2], 
[1, 2, '-', 3, '-', 2, 1], 
[2, '-', '-', 2, '-', 1, 2], 
[3, '-', 2, 1, 2, 2, 3], 
[3, 2, 1, 2, 1, '-', '-'], 
[4, '-', 2, 1, 2, 3, 4], 
[5, '-', 3, 2, 3, 4, 5]]

[[0, 1, 2, 3, -1, -1, 2], 
[1, 2, -1, 3, -1, 0, 1], 
[2, -1, -1, 2, -1, 1, 2], 
[3, -1, 2, 1, 2, 2, 3], 
[3, 2, 1, 0, 1, -1, -1], 
[4, -1, 2, 1, 2, 3, 4], 
[5, -1, 3, 2, 3, 4, 5]]



"""
