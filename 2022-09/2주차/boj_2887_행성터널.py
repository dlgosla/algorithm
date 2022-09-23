"""
최소 신장 트리 만들기
"""

import sys

# 노드가 어느 집합에 속하는 지 찾기
def find_parent(n):
    if parents[n] != n:
        parents[n] = find_parent(parents[n])

    return parents[n]


# a,b를 같은 집합으로 만들기
def union(a, b):
    a = find_parent(a)
    b = find_parent(b)

    if a < b:
        parents[b] = a
    else:
        parents[a] = b


input = sys.stdin.readline
n = int(input())

parents = [0] * n
planets = []

for i in range(n):
    x, y, z = map(int, input().split())
    planets.append((x, y, z, i))  # 좌표, 노드 번호

    parents[i] = i

# 간선 정보
edges = []

# 정점을 돌면서 모든 간선을 찾는 로직 => 메모리 초과
# for i in range(n):
#     x, y, z = planets[i]

#     for j in range(i + 1, n):
#         nx, ny, nz = planets[j]
#         # cost = min(abs(nx - x), abs(ny - y), abs(nz - z))

#         # edges.append((cost, i, j))

# 필요한 간선 후보들만 가져오는 로직
# 각 축을 기준으로 정렬 후 n개의 간선만 고려
for i in range(3):
    temp_edges = sorted(planets, key=lambda x: x[i])

    for j in range(n - 1):
        edges.append(
            (
                abs(temp_edges[j][i] - temp_edges[j + 1][i]),
                temp_edges[j][3],
                temp_edges[j + 1][3],
            )
        )

# 비용 기준으로 정렬
edges.sort()

count = 0
min_cost = 0
for cost, a, b in edges:
    # 간선 개수가 n-1이 되면 종료
    if count == n - 1:
        break

    # 같은 집합이 아니면 트리로 만들 수 있음
    if find_parent(a) != find_parent(b):
        # 같은 집합으로 만듦
        union(a, b)
        count += 1
        min_cost += cost

print(min_cost)
