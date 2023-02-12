"""
순서대로 나와야함 -> 우선순위큐

"""
from heapq import heappush, heappop
import sys

input = sys.stdin.readline
t = int(input())


for i in range(t):
    n, m = map(int, input().split())
    rain_lst = list(map(int, input().split()))

    hq = []

    next_rain_time = [[] for _ in range(m + 1)]
    for i in range(m - 1, -1, -1):
        rainy_lake = rain_lst[i]
        if rainy_lake:
            next_rain_time[rainy_lake].append(i)

    for lake in range(1, m + 1):
        if next_rain_time[lake]:
            heappush(hq, (next_rain_time[lake].pop(), lake))

    drinking = []
    is_full = [True for _ in range(n + 1)]
    disaster = False
    for rainy_lake in rain_lst:

        if not rainy_lake:
            # 차있는 호수 중에 다음에 가장 빨리 비가 올 호수를 찾아서 먹음
            if hq:
                _, next_lake_to_rain = heappop(hq)
                is_full[next_lake_to_rain] = False
                drinking.append(next_lake_to_rain)
            else:
                drinking.append(0)

        else:
            # 빈 호수에 비가 오면
            if not is_full[rainy_lake]:
                is_full[rainy_lake] = True
                # 다음에 이 호수에 비가 올 시간을 저장
                # -> 호수가 무조건 차 있게 되기 때문에 힙에서 바로 빼도 됨
                if next_rain_time[rainy_lake]:
                    heappush(hq, (next_rain_time[rainy_lake].pop(), rainy_lake))

            # 가득 찬 호수에 비가 오면 실패
            else:
                disaster = True
                break

    if disaster:
        print("NO")
    else:
        print("YES")
        print(*drinking)

"""
1
2 4
0 1 0 2

1
2 6
0 0 1 0 1 2


1
2 6
0 0 0 1 0 1
"""
