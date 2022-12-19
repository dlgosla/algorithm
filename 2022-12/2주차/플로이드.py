n = int(input())
m = int(input())

graph = [[0 if i == j else float("inf") for j in range(n)] for i in range(n)]
# print(graph)

for i in range(m):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    graph[a][b] = min(graph[a][b], c)

for k in range(n):
    for a in range(n):
        for b in range(n):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for i in range(n):
    for j in range(n):
        cost = 0 if graph[i][j] == float("inf") else graph[i][j]
        print(cost, end=" ")
    print()
