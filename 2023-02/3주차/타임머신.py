"""
한 도시에서 다른 모든 도시까지 가는데 최소거리 (음수 간선 포함)
-> 밸만포드

"""

n, m = map(int, input().split())

edges = []
for i in range(m):
    start, end, cost = map(int, input().split())
    start -= 1
    end -= 1
    edges.append((start, end, cost))

dist = [float("inf") for i in range(n)]
dist[0] = 0

nagative_cycle = False
for i in range(n):
    for (curr, next, cost) in edges:
        if dist[curr] != float("inf") and dist[next] > dist[curr] + cost:
            dist[next] = dist[curr] + cost

            if i == n - 1:
                nagative_cycle = True

if nagative_cycle:
    print(-1)
else:
    for i in range(1, n):
        if dist[i] == float("inf"):
            print(-1)
        else:
            print(dist[i])
