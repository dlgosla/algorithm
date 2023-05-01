from collections import defaultdict
from heapq import heapify, heappop, heappush


def solution(n, costs):

    total_cost = 0
    graph = defaultdict(list)
    start_node = None
    for [n1, n2, cost] in costs:
        if start_node == None:
            start_node = n1
        graph[n1].append((cost, n2))
        # graph[n2].append((cost, n1))

    adjacent_nodes = graph[start_node][:]
    heapify(adjacent_nodes)
    visited = []

    while adjacent_nodes:
        cost, min_cost_adjacent_node = heappop(adjacent_nodes)

        if min_cost_adjacent_node not in visited:
            total_cost += cost
            visited.append(min_cost_adjacent_node)

        for (next_cost, next_node) in graph[min_cost_adjacent_node]:
            if next_node not in visited:
                heappush(adjacent_nodes, (next_cost, next_node))

    return total_cost


print(solution(4, [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]]))
