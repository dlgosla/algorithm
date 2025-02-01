"""

최대 2개 활성화 시킬 수 있다면

0 0 * 0
0 0 - 0 
* - - *

(0,2)부터 퍼졌을 경우
2 1 * 1
3 2 - 2 
4 - - 3

(2,0)부터 퍼졌을 경우
2 3 4 5
1 2 - 6 
* - - 7

(2,3)부터 퍼졌을 경우
5 4 3 2
6 5 - 1 
7 - - *

가능한 조합
(0,2), (2,0) 활성화
(0,2), (2,3) 활성화
(2,0), (2,3) 활성화

(0,2), (2,0) 활성화 시켰을 경우 활성 상태
=> (0,2)부터 퍼졌을 경우와 (2,0)부터 퍼졌을 경우를 비교해서 맵을 만듦
2 1 * 1
1 2 - 2 
* - - *


이 활성상태 맵에서 가장 큰 값을 구하면 그게 그 조합에서 
모든 칸에 바이러스를 퍼트릴 수 있는 최소 시간이 된다.

나머지도 조합에서도 똑같이 구하고 조합 중에 최솟값을 구하면 답이 된다.
단 어떤 하나의 칸이라도 0으로 남아있으면 바이러스가 퍼지지 못한다는 뜻이므로 이 경우는 최솟값 계산에서 제외한다.
모든 조합에서 다 그러면 -1을 리턴한다.

"""


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
