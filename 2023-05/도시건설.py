from heapq import heappop, heappush


def find_parent(a):
    global parents

    if parents[a] == a:
        return a

    return find_parent(parents[a])


def union(a, b):
    global parents

    a = find_parent(a)
    b = find_parent(b)

    if a < b:
        parents[b] = a
    else:
        parents[a] = b


n, m = map(int, input().split())
edges = []
parents = [i for i in range(n)]
total_cost = 0

for i in range(m):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    # edges.append((c, a, b))
    heappush(edges, (c, a, b))
    total_cost += c

# print(edges)
min_cost = 0
included_nodes = 0
while included_nodes < n and edges:
    c, a, b = heappop(edges)

    if find_parent(a) != find_parent(b):
        union(a, b)
        min_cost += c
        included_nodes += 1


if included_nodes + 1 < n:
    print(-1)
else:
    print(total_cost - min_cost)
