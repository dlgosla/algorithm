"""
뭔가 모양 만들 때 dfs, bfs같은 거 생각해보기
그리고 모양 만들 때 안되면 뭔가를 추가하는 게 아니라 빼는 방법도 생각해보기

"""
from collections import deque

n, m = map(int, input().split())

# hq = []
dq = deque()
visited = []
map = []
for i in range(n):
    lst = [int(i) for i in input().split()]
    map.append(lst)

max_score = 0
# dq.append((0, 0, 0, 0))
# visited.append((0, 0))


delta = [(0, 1), (0, -1), (1, 0), (-1, 0)]
for i in range(n):
    for j in range(m):
        dq.append((i, j, 1, map[i][j], [(i, j)]))

        while dq:
            (cr, cc, count, score, path) = dq.pop()

            if count == 4:
                if max_score < score:
                    max_score = score
                continue

            for dr, dc in delta:
                nr = cr + dr
                nc = cc + dc

                if not (0 <= nr < n and 0 <= nc < m):
                    continue

                if (nr, nc) not in path:
                    dq.append(
                        (nr, nc, count + 1, score + map[nr][nc], path + [(nr, nc)])
                    )

        total_cross_score = map[i][j]
        cross_count = 1
        min_cross_score = 1e9
        for dr, dc in delta:
            nr = i + dr
            nc = j + dc

            if not (0 <= nr < n and 0 <= nc < m):
                continue

            cross_score = map[nr][nc]
            if cross_score < min_cross_score:
                min_cross_score = cross_score

            total_cross_score += cross_score
            cross_count += 1

        # print(total_cross_score, cross_count, min_cross_score)
        if cross_count == 5:
            total_cross_score -= min_cross_score

        elif cross_count < 4:
            continue

        if total_cross_score > max_score:
            max_score = total_cross_score

print(max_score)
