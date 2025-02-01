import heapq
from collections import defaultdict

n, d = map(int, input().split())
nodes = set()

nodes.add(d)
graph = defaultdict(list)


for i in range(n):
    start, end, weight = map(int, input().split())
    graph[start].append((end, weight))
    
    nodes.add(start)
    nodes.add(end)

nodes = list(nodes)
nodes.sort()
privious = 0 

for node in nodes:
    dist = node - privious
    graph[privious].append((node, dist))
    privious = node

dist = {node: float('inf') for node in nodes}
dist[0] = 0

hq = []
heapq.heappush(hq, (dist[0], 0))

while hq:
    curr_dist, curr_node = heapq.heappop(hq)
    if (curr_dist > dist[curr_node]):
        continue
    else:
        for (adjacent, weight) in graph[curr_node]:
            new_dist = curr_dist + weight

            if (new_dist < dist[adjacent]):
                dist[adjacent] = new_dist
                heapq.heappush(hq, (new_dist, adjacent))


print(dist[d])
