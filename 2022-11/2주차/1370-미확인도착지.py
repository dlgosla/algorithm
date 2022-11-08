"""
특정 간선을 반드시 지나는 최단 경로 찾기

"""


import sys
from collections import defaultdict
import heapq

input = sys.stdin.readline

T = int(input())

for i in range(T):
    graph = defaultdict(list)
    possible_destination_lst = []

    # 교차로, 목적지, 목적지 후보 개수
    n, m, t = map(int, input().split())

    # 출발지, 반드시 (g,h)를 지남
    s, g, h = input().split()
    s = int(s)

    smell_roads = [g + h, h + g]

    # 도로
    for _ in range(m):
        # a,b 노드 사이 길이 d 도로
        a, b, d = input().split()
        d = int(d)

        if a + b in smell_roads:
            d -= 0.01

        a = int(a)
        b = int(b)

        graph[a].append((b, d))
        graph[b].append((a, d))

    for _ in range(t):
        possible_destination_lst.append(int(input()))

    min_dist = [float("inf") for i in range(0, n + 1)]
    min_dist[s] = 0

    hq = []
    heapq.heappush(hq, (min_dist[s], s, ""))
    route = ["" for i in range(0, n + 1)]

    while hq:
        curr_dist, curr_n, path = heapq.heappop(hq)

        if min_dist[curr_n] < curr_dist:
            continue

        for item in graph[curr_n]:
            next_n, next_dist = item

            new_dist = curr_dist + next_dist

            if new_dist < min_dist[next_n]:
                min_dist[next_n] = new_dist

                new_path = path + str(curr_n)
                route[next_n] = new_path

                heapq.heappush(hq, (new_dist, next_n, new_path))

    answer = []
    for dest in possible_destination_lst:
        if type(min_dist[dest]) == float and min_dist[dest] != float("inf"):
            answer.append(dest)

    print(*sorted(answer))
